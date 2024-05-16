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
    
    
    full_path: str = field(compare=False, hash=True)
    name: str = field(compare=False, hash=True)
    text: str = field(compare=False)
    entities: List[Entity] = field(default_factory=list, compare=False)
    relations: List[Relation] = field(default_factory=list, compare=False)
    
    @property
    def entity_labels(self):
        """
        Returns a set of all entity labels in the document.
        """
        return {entity.label for entity in self.entities}
    
    @property
    def relation_labels(self):
        """
        Returns a set of all relation labels in the document.
        """
        return {relation.label for relation in self.relations}
    
    def as_entity_list(self) -> List[Entity]:
        """
        Returns a list of all entities in the document.
        """
        last_end = 0
        entities = []
        for word in self.text.split():
            for entity in self.entities:
                if entity.start == last_end:
                    entities.append(entity)
                    last_end = entity.end
                else:
                    entities.append(Entity(-1, 'O', last_end + 1, last_end + len(word), word))
                    last_end += len(word)
        return entities
    
    