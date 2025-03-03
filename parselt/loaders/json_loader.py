from parselt import DocumentLoader, Document
import json
import os


class JSONAnnotationSchema:
    """
    Defines a schema for parsing JSON annotations.

    This class specifies the key mappings for extracting text, entities, 
    and relationships from JSON annotation files. It provides a default schema 
    but allows for customization by modifying the class attributes.

    Attributes:
        file_key (str): Key for identifying the document or file name in the JSON.
        text_key (str): Key for retrieving the annotated text.
        entity_key (str): Key for accessing the list of entities.
        relationship_key (str): Key for accessing the list of relationships.
        entity_fields (dict[str, str]): Mapping of entity attributes to JSON keys.
        relationship_fields (dict[str, str]): Mapping of relationship attributes to JSON keys.
    """

    file_key: str = "document"

    text_key: str = "text"
    entity_key: str = "entities"
    relationship_key: str = "relations"
    entity_fields: dict[str, str] = {
        "id": "id",
        "label": "label",
        "text": "text",
        "start": "start",
        "end": "end"
    }

    relationship_fields: dict[str, str] = {
        "id": "id",
        "type": "type",
        "arg1": "arg1",
        "arg2": "arg2"
    }


class JSONLoader(DocumentLoader):
    """
    A loader for reading JSON files containing text and annotations.

    This class loads JSON data from a given file and can optionally retrieve 
    text from external `.txt` files stored in a specified directory.

    Attributes:
        text_dir (str | None): Directory containing text files referenced in the JSON.
        load_txt_files (bool): Whether to load text from external `.txt` files.

    Raises:
        ValueError: If `load_txt_files` is True but `text_dir` is not provided.
    """

    def __init__(self, text_dir: str | None = None, 
                 load_txt_files: bool = False,
                 custom_schema: JSONAnnotationSchema = None) -> None:
        """
        Initializes the JSONLoader.

        Args:
            text_dir (str | None, optional): Path to the directory containing text files. 
                Required if `load_txt_files` is True. Defaults to None.
            load_txt_files (bool, optional): Whether to load text from external `.txt` files. 
                Defaults to False.
            custom_schema (JSONAnnotationSchema, optional): Custom schema for parsing JSON annotations.
                Defaults to None.
        """
        
        self.text_dir = text_dir
        self.load_txt_files = load_txt_files

        if self.load_txt_files and self.text_dir is None:
            raise ValueError("If load_txt_files is True, text_dir must be provided.")

        self.default_schema: JSONAnnotationSchema = custom_schema if custom_schema is not None else JSONAnnotationSchema()

    def load_file(self, file_path: str) -> Document | list[Document]:
        """
        Loads JSON data from the specified file.

        Args:
            file_path (str): Path to the JSON file to be loaded.

        Returns:
            dict: Parsed JSON data.
        """
        
        if not file_path.endswith(".json"):
            raise ValueError("Invalid file format. Expected a JSON file.")
        
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        
        if isinstance(data, list):
            docs = []
            for doc_obj in data:
                docs.append(self.parse_json_document(doc_obj))
            return docs
        elif isinstance(data, dict):
            return self.parse_json_document(data)
        else:
            raise ValueError("Invalid JSON format. Expected a dictionary or a list of dictionaries.")
        
        
    def parse_json_document(self, data: dict) -> Document:
        """
        Parses JSON data into a Document object.

        Args:
            data (dict): JSON data containing text and annotations.

        Returns:
            Document: Parsed document object.
        """
        
        text = None
        if self.load_txt_files:
            with open(os.path.join(self.text_dir, data[self.default_schema.file_key]), "r", encoding="utf-8") as text_file:
                text = text_file.read()
        else:
            text = data[self.default_schema.text_key]
        
        entities = self._parse_entities(data)
        relations = self._parse_relations(data, entities)
        
        document = Document(id=data[self.default_schema.file_key], path=data[self.default_schema.file_key], text=text, entities=entities, relations=relations)
        return document
        
    def _parse_entities(self, data: dict) -> list[dict]:
        """
        Parses entity annotations from the JSON data.

        Args:
            data (dict): JSON data containing entity annotations.

        Returns:
            list[dict]: List of parsed entity annotations.
        """
        
        entities = data[self.default_schema.entity_key]
        parsed_entities = []
        
        for entity in entities:
            parsed_entity = {
                key: entity[value] for key, value in self.default_schema.entity_fields.items()
            }
            parsed_entities.append(parsed_entity)
        
        return parsed_entities
    
    def _parse_relations(self, data: dict, entities: list[dict]) -> list[dict]:
        """
        Parses relationship annotations from the JSON data.

        Args:
            data (dict): JSON data containing relationship annotations.
            entities (list[dict]): List of parsed entity annotations.

        Returns:
            list[dict]: List of parsed relationship annotations.
        """
        
        relations = data[self.default_schema.relationship_key]
        parsed_relations = []
        
        for relation in relations:
            parsed_relation = {
                key: relation[value] for key, value in self.default_schema.relationship_fields.items()
            }
            parsed_relations.append(parsed_relation)
        
        return parsed_relations
        

