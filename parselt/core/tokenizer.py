from abc import ABC, abstractmethod
from parselt.core.token import Token

class Tokenizer(ABC):
    """
    An abstract base class for tokenizers, defining the interface for tokenization.
    """
    
    @abstractmethod
    def tokenize(self, text: str) -> list[Token]:
        """
        Tokenize the input text into a list of tokens.
        
        Args:
            text (str): The text to tokenize.
            
        Returns:
            list[Token]: A list of tokens.
        """
        pass
    
    def preprocess(self, text: str, lower: bool) -> str:
        """
        Preprocess the input text before tokenization.
        
        Args:
            text (str): The text to preprocess.
            
        Returns:
            str: The preprocessed text.
        """
        
        if lower:
            text = text.lower()
        return text

    
