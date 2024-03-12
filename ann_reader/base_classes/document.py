from dataclasses import dataclass, field
from ann_reader.base_classes.entity import Entity
from ann_reader.base_classes.relation import Relation
from typing import List

@dataclass(unsafe_hash=True)
class Document:
    '''
    A class to represent a document and its annotations.
    Takes four arguments:
    - path: str, the path to the document file.
    - text: str, the text of the document.
    - entities: list, a list of Entity objects.
    - relations: list, a list of Relation objects.
    '''
    
    
    path: str = field(compare=False, hash=True)
    text: str = field(compare=False)
    entities: List[Entity] = field(default_factory=list, compare=False)
    relations: List[Relation] = field(default_factory=list, compare=False)
    
    
    
    
    
    