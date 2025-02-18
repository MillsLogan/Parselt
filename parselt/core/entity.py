from parselt.core.token import Token

class Entity(Token):
    def __init__(self, text: str, start: int, end: int, label: str, entity_id: int) -> None:
        """
        Initializes an Entity object.

        Args:
            text (str): The text of the entity.
            start (int): The start index of the entity in the document.
            end (int): The end index of the entity in the document.
            label (str): The label of the entity.
            entity_id (int): The unique ID of the entity.
        """
        
        super().__init__(text, start, end)
        self.label: str = label
        self.entity_id: int = entity_id
        
    def __repr__(self) -> str:
        """
        Returns a string representation of the Entity object.
        """
        return f'Entity({self.label}, {self.entity_id}, {self.start}, {self.end}, "{self.text}")'
    
    
    