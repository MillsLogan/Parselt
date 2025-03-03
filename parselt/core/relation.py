from __future__ import annotations
from dataclasses import dataclass
from parselt.core.entity import Entity


@dataclass
class Relation:
    """
    Represents a relation between two entities in a document.
    
    Attributes:
        id (int): The unique ID of the relation.
        label (str): The label of the relation.
        arg_1 (Entity): The first argument (entity) of the relation.
        arg_2 (Entity): The second argument (entity) of the relation.
    """
    
    id: int
    label: str
    arg_1: Entity
    arg_2: Entity
    
    def __post_init__(self):
        """
        Checks that tokens are not None.
        """
        
        if not isinstance(self.arg_1, Entity) or not isinstance(self.arg_2, Entity):
            raise ValueError("Arguments must be entities.")
    
    def __str__(self):
        return f'R{self.id}\t{self.label} Arg1:T{self.arg_1.entity_id} Arg2:T{self.arg_2.entity_id}'


        