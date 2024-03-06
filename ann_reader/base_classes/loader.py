from abc import ABC, abstractmethod


class Loader(ABC):
    '''
    Abstract base class for loading datasets into Document objects.
    '''
    
    def __init__(self):
        self.dataset = {}
    
    def __call__(self, document_path: str, annotation_path: str = None):
        self.load()
        
    @abstractmethod
    def load(self, document_path: str, annotation_path: str = None):
        pass
    
    @abstractmethod
    def _create_document(self, document_path: str, annotation_path: str):
        pass
    
    def __iter__(self):
        return iter(self.dataset.items())
    
    def __getitem__(self, key):
        return self.dataset[key]
    
    def __setitem__(self, key, value):
        self.dataset[key] = value
        
    def __delitem__(self, key):
        del self.dataset[key]
        
    def __len__(self):
        return len(self.dataset)
    
    def __contains__(self, key):
        return key in self.dataset
    
    def __str__(self):
        return str(self.dataset)
    
    
