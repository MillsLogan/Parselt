from __future__ import annotations
from parselt.core.document_loader import DocumentLoader
from parselt.core.document import Document
import os
from parselt.core.relation import Relation
from parselt.core.entity import Entity


class BratLoader(DocumentLoader):
    """
    A class for loading documents from the BRAT format.
    
    Args:
        text_dir (str | None): Optional directory containing text files. If None, the text files are expected to be in the same directory as the annotations.
    """
    
    def __init__(self, text_dir: str | None=None) -> None:
        self.text_dir = text_dir
        
    def load_file(self, document_path: str) -> Document | None:
        """
        Load a single document from a BRAT formatted ".ann" file.
        
        Args:
            document_path (str): The path to the ".ann" file.
            
        Returns:
            Document | None: The loaded document, or None if the file could not be loaded.
        """
        
        if not document_path.endswith(".ann"):
            return None
        
        named_entities = []
        relations = []
        
        # Load the annotation file
        with open(document_path, "r", encoding="utf-8") as ann_file:
            for line in ann_file:
                if line.startswith("T"):
                    named_entities.append(self._parse_term(line))
                elif line.startswith("R"):
                    relations.append(self._parse_relation(line, named_entities))
                
                
        # Load the text file
        text_file_path = document_path.replace(".ann", ".txt")
        if self.text_dir:
            text_file_path = os.path.join(self.text_dir, os.path.basename(text_file_path))
            
        with open(text_file_path, "r", encoding="utf-8") as text_file:
            text = text_file.read()
        
        # Create a Document object
        document = Document(id=os.path.basename(document_path), path=document_path, 
                            text=text, entities=named_entities, relations=relations)
        return document
                
    def _parse_relation(self, line: str, named_entities: list[Entity]) -> Relation:
        """
        Parse a relation line from the annotation file.
        
        Args:
            line (str): The line to parse.
            named_entities (list[Entity]): The list of named entities.
            
        Returns:
            Relation: The parsed relation.
        """
        
        parts = line.strip().split("\t")
        relation_id = int(parts[0][1:])
        label = parts[1]
        arg_1, arg_2 = parts[2].split(" ")
        
        arg_1_id = int(arg_1[1:])
        arg_2_id = int(arg_2[1:])
        
        arg_1_token = next((entity for entity in named_entities if entity.entity_id == arg_1_id), None)
        arg_2_token = next((entity for entity in named_entities if entity.entity_id == arg_2_id), None)
        
        return Relation(relation_id, label, arg_1_token, arg_2_token)
                    
    def _parse_term(self, line: str) -> Entity:
        """
        Parse a term line from the annotation file.
        
        Args:
            line (str): The line to parse.
            
        Returns:
            Entity: The parsed entity.
        """
        
        parts = line.strip().split("\t")
        entity_id = int(parts[0][1:])
        label, start, end = parts[1].split(" ")
        text = parts[2]
        
        return Entity(text, int(start), int(end), label=label, entity_id=entity_id)
            
        
        