class Token:
    """
    A class representing a token in a document.
    
    Args:
        text (str): The text of the token.
        start (int): The start index of the token in the document.
        end (int): The end index of the token in the document.
        next_char (str | None): The next character after the token, if any, defaults to " ".
        label (str | None): The label of the token, if any.
    """
    
    def __init__(self, text: str, start: int, end: int, 
                    next_char: str | None=None):
        
        self.text: str = text
        self.start: int = start
        self.end: int = end
        self.next_char: str = next_char if next_char is not None else " "
        self.label: str | None = None
        
    def __hash__(self) -> int:
        """
        Returns a hash of the token based on its text, start, end, label, and entity_id.
        """
        
        return hash((self.text, self.start, self.end))
    
    def __eq__(self, other: object) -> bool:
        """
        Checks if two tokens are equal based on their text, start, end, label, and entity_id.
        
        Args:
            other (object): The other object to compare with.
        """
        
        if not isinstance(other, Token):
            return NotImplemented
        
        return (self.text, self.start, self.end) == \
               (other.text, other.start, other.end)
        
    def __str__(self) -> str:
        return f'{self.text} ({self.start}, {self.end})'