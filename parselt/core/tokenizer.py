from abc import ABC, abstractmethod
from parselt.core.token import Token
import re

class Tokenizer(ABC):
    """
    An abstract base class for tokenizers, defining the interface for tokenization.
    """
    
    def __init__(self, lower: bool = False, remove_punctuation: bool = False,
                 normalize_whitespace: bool = False, remove_stopwords: bool = False,
                 tokenize_numbers: bool = False) -> None:
        """
        Initialize the tokenizer.
        
        Args:
            lower (bool): Whether to convert text to lowercase before tokenization.
            remove_punctuation (bool): Whether to remove punctuation from the text.
            normalize_whitespace (bool): Whether to normalize whitespace in the text.
            remove_stopwords (bool): Whether to remove stopwords from the text.
            tokenize_numbers (bool): Whether to tokenize numbers as separate tokens.
        """
        
        self.lower = lower
        self.remove_punctuation = remove_punctuation
        self.normalize_whitespace = normalize_whitespace
        self.remove_stopwords = remove_stopwords
        self.tokenize_numbers = tokenize_numbers
    
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
    
    def preprocess(self, text: str) -> str:
        """
        Preprocess the input text before tokenization.
        
        Args:
            text (str): The text to preprocess.
            
        Returns:
            str: The preprocessed text.
        """
        
        if self.lower:
            text = text.lower()
        if self.remove_punctuation:
            text = ''.join(char for char in text if char.isalnum() or char.isspace())
        if self.normalize_whitespace:
            text = re.sub(r'\s+', ' ', text).strip()
        if self.remove_stopwords:
            # Placeholder for stopword removal logic
            pass
        if self.tokenize_numbers:
            # Placeholder for number tokenization logic
            pass
        
        return text

    
