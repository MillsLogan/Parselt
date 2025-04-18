from parselt import Document, Entity, Relation
from parselt.loaders.base_loader import BaseLoader
import json
import os
from intervaltree import Interval, IntervalTree


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


class JSONLoader(BaseLoader):
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
                docs.append(self.parse_json_document(doc_obj, file_path))
            return docs
        elif isinstance(data, dict):
            return self.parse_json_document(data, file_path)
        else:
            raise ValueError("Invalid JSON format. Expected a dictionary or a list of dictionaries.")
        
        
    def parse_json_document(self, data: dict, file_path: str) -> Document:
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
        
        doc_id = os.path.basename(data[self.default_schema.file_key].split(".")[0])
        
        document = Document(id=doc_id, path=file_path, text=text, entities=entities, relations=relations)
        return document
        
    def _parse_entities(self, data: dict) -> list[Interval]:
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
            entity_id = entity[self.default_schema.entity_fields["id"]]
            entity_label = entity[self.default_schema.entity_fields["label"]]
            entity_text = entity[self.default_schema.entity_fields["text"]]
            entity_start = entity[self.default_schema.entity_fields["start"]]
            entity_end = entity[self.default_schema.entity_fields["end"]]
            parsed_entities.append(Interval(begin=entity_start, end=entity_end, data=Entity(entity_text, entity_start, entity_end, label=entity_label, entity_id=entity_id)))
        
        return parsed_entities
    
    def _parse_relations(self, data: dict, entity_intervals: list[Interval]) -> list[dict]:
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
            relation_id = relation[self.default_schema.relationship_fields["id"]]
            relation_type = relation[self.default_schema.relationship_fields["type"]]
            arg1_id = relation[self.default_schema.relationship_fields["arg1"]]
            arg2_id = relation[self.default_schema.relationship_fields["arg2"]]
            
            arg1_token = None
            arg2_token = None
            for interval in entity_intervals:
                entity: Entity = interval.data
                assert isinstance(entity, Entity)
                if entity.entity_id == arg1_id:
                    arg1_token = entity
                elif entity.entity_id == arg2_id:
                    arg2_token = entity
                if arg1_token and arg2_token:
                    break
            else:
                raise ValueError(f"Entities {arg1_id} and {arg2_id} not found in the document.")
            
            
            parsed_relation = Relation(relation_id, relation_type, arg1_token, arg2_token)
            parsed_relations.append(parsed_relation)
        
        return parsed_relations
        

