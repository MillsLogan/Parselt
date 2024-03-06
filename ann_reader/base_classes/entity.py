from dataclasses import dataclass, field


@dataclass
class Entity:
    '''
    Base class for an entity in a document.
    Takes five arguments:
    - id: int, the id of the entity.
    - type: str, the type of the entity.
    - start: int, the start index of the entity.
    - end: int, the end index of the entity.
    - text: str, the text of the entity.
    '''
    
    id: int
    type: str
    start: int
    end: int
    text: str
    
    def __str__(self):
        return f'T{self.id}\t{self.type} {self.start} {self.end}\t{self.text}'
    
        
        