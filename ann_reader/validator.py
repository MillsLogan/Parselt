from ann_reader import Document, Entity
from ann_reader.base_classes.loader import Loader

class Validator:
    def __init__(self, case_sensitive: bool=True):
        '''
        Initialize a Validator object.
        Takes three optional arguments:
            - case_sensitive: bool - Whether the
            text in the document and the text in the
            entity annotation should match exactly.
        '''
        self.case_sensitive = case_sensitive
        
    def __call__(self, dataset: Loader) -> dict[Document, list[Entity]]:
        '''
        Call the object as a function to validate an entity annotation in a document.
        Takes one argument:
            - dataset: Loader - The dataset to validate the entity in.
        Returns a dictionary with the document as the key and a list of valid entities as the values.
        '''
        return self.validate(dataset)
        
    def validate(self, dataset: Loader) -> dict[Document, list[Entity]]:
        '''
        Validate all entities in the dataset.
        Takes one argument:
            - dataset: Loader - The dataset to validate the entity in.
        Returns a dictionary with the document as the key and a list of valid entities as the values.
        NOTE: No changes are made to the dataset, the entities are simply filtered and returned.
        '''
        valid_dataset = {}
        for document in dataset:
            valid_entities = []
            for entity in document.entities:
                if self._validate_entity(document, entity):
                    valid_entities.append(entity)
            valid_dataset[document] = valid_entities
            
        return valid_dataset
                
        
            
    def _validate_entity(self, document: Document, entity: Entity):
        '''
        Private method to validate an entity in a document.
        Validate an entity annotation in a document.
        Takes two arguments:
            - document: Document - The document to validate the entity in.
            - entity: Entity - The entity to validate.
        Returns a bool indicating whether the entity is valid.
        '''
        if self.case_sensitive:
            return entity.text == document.text[entity.start:entity.end]
        return entity.text.lower() == document.text[entity.start:entity.end].lower()
        
        
        
        