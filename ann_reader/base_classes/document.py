from dataclasses import dataclass, field


@dataclass
class Document:
    '''
    A class to represent a document and its annotations.
    Takes four arguments:
    - path: str, the path to the document file.
    - text: str, the text of the document.
    - entities: list, a list of Entity objects.
    - relations: list, a list of Relation objects.
    '''
    
    
    path: str
    text: str
    entities: list = field(default_factory=list)
    relations: list = field(default_factory=list)
    
    
    
    
    