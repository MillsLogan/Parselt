from abc import ABC, abstractmethod
from ann_reader.base_classes.document import Document
from typing import List
import os


class Loader(ABC):
    '''
    Abstract base class for loading datasets into Document objects.
    '''
    
    def __init__(self):
        self.dataset = {}
    
    def __call__(self, document_path: str, annotation_path: str = None) -> Document | List[Document]:
        if os.path.isdir(document_path):
            return self.load_all(document_path, annotation_path)
        return self.load(document_path, annotation_path)
        
    @abstractmethod
    def load(self, document_path: str, annotation_path: str = None) -> Document:
        pass
    
    @abstractmethod
    def _create_document(self, document_path: str, annotation_path: str) -> List[Document]:
        pass
    
    @abstractmethod
    def load_all(self, document_dir: str, annotation_dir: str = None) -> List[Document]:
        pass
    
    def __iter__(self) -> iter:
        return iter(self.dataset.values())
    
    @property
    def documents(self) -> List[Document]:
        return self.dataset.values()
    
    def __getitem__(self, key) -> Document:
        return self.dataset[key]
    
    def __setitem__(self, key, value) -> None:
        self.dataset[key] = value
        
    def __delitem__(self, key) -> None:
        del self.dataset[key]
        
    def __len__(self) -> int:
        return len(self.dataset)
    
    def __contains__(self, key) -> bool:
        return key in self.dataset
    
    def __str__(self) -> str:
        return str(self.dataset)
    
    
