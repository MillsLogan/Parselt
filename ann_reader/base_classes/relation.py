from dataclasses import dataclass
from ann_reader.base_classes.entity import Entity


@dataclass
class Relation:
    '''
    A class to represent a relation between two entities in a document.
    Takes six arguments:
    - id: int, the id of the relation.
    - type: str, the type of the relation.
    - start: int, the start index of the relation.
    - end: int, the end index of the relation.
    - arg_1: Entity, the first entity involved in the relation.
    - arg_2: Entity, the second entity involved in the relation.
    '''
    
    id: int
    type: str
    start: int
    end: int
    arg_1: Entity
    arg_2: Entity
    
    def __str__(self):
        return f'R{self.id}\t{self.type} Arg1:T{self.arg_1.id} Arg2:T{self.arg_2.id}'


        