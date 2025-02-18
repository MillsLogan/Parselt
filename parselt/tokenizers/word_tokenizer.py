from parselt.core.tokenizer import Tokenizer
from parselt.core.token import Token
import re

class WordTokenizer(Tokenizer):
    """
    Tokenizer that splits text into words based on whitespace and punctuation.
    """
    
    def tokenize(self, text: str) -> list[Token]:
        """
        Tokenize the input text into a list of tokens.
        
        Args:
            text (str): The text to tokenize.
            
        Returns:
            list[Token]: A list of tokens.
        """
        
        tokens = []
        previous_tok: Token = None
        for match in re.finditer(r"\b[\w’-]+\b", text):
            start, end = match.span()
            token_text = match.group(0)
            token = Token(text=token_text, start=start, end=end, next_char=text[end:end+1])
            tokens.append(token)
            if previous_tok is not None:
                previous_tok.next_char = text[previous_tok.end:start]
            previous_tok = token
        
        return tokens
    