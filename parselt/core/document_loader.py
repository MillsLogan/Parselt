from abc import ABC, abstractmethod
from parselt.core.document import Document
from typing import Generator
import os
from pathlib import Path

class DocumentLoader(ABC):
    """
    Abstract base class for loading documents from files.
    """
    
    @abstractmethod
    def load_file(self, document_path: str) -> Document | None:
        """
        Load a single document from a file.
        
        Args:
            document_path (str): The path to the document file.
            
        Returns:
            Document | None: The loaded document, or None if the file could not be loaded.
        """
        
        pass
    
    def load_directory(self, directory_path: str) -> Generator[Document, None, None]:
        """
        Lazily load documents from a directory.
        
        Args:
            directory_path (str): The path to the directory containing document files.
            
        Yields:
            Document: The loaded document.
        """
        
        path = Path(directory_path)
        if not path.is_dir():
            raise ValueError(f"{directory_path} is not a directory.")
        
        for file in os.listdir(path):
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                document = self.load_file(file_path)
                if document:
                    yield document
                    
        
            
        
