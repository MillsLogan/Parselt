from __future__ import annotations
from ann_reader.core.token import Token
from ann_reader.core.relation import Relation
from ann_reader.core.entity import Entity

class Document:
    """
    A class representing a document with text and annotations.
    
    Attributes:
        id (int): The unique ID of the document.
        path (str): The path to the document.
        text (str): The text of the document.
        entities (list): A list of named entities in the document.
        relations (list): A list of relations in the document.
        tokens (list): A list of tokens in the document, as processed by a Tokenizer.    
    """
    
    def __init__(self, id: int, path: str, text: str, entities: list, relations: list, tokens: list | None=None) -> None:
        self.id: int = id
        self.path: str = path
        self.text: str = text
        self.relations: list[Relation] = relations
        self.entities: list[Entity] = entities
        self.tokens: list[Token] = tokens if tokens is not None else []
        
    @property
    def is_tokenized(self) -> bool:
        """
        Checks if the document is tokenized.
        
        Returns:
            bool: True if the document is tokenized, False otherwise.
        """
        
        return len(self.tokens) > 0
    
    def tokenize(self, tokenizer: "Tokenizer") -> None:
        """
        Tokenizes the document using the provided tokenizer.
        
        Args:
            tokenizer (Tokenizer): The tokenizer to use for tokenization.
        """
        
        self.tokens = tokenizer.tokenize(self.text)

    def entity_labels(self) -> set[str]:
        """
        Returns a set of unique entity labels in the document.
        """
        
        return {entity.label for entity in self.entities}
    
    def relation_labels(self) -> set[str]:
        """
        Returns a set of unique relation labels in the document.
        """
        
        return {relation.label for relation in self.relations}
        
    def __iter__(self):
        """
        Returns an iterator over the tokens in the document.
        """
        
        return iter(self.tokens)
    
    def __getitem__(self, index: int) -> Token:
        """
        Returns the token at the specified index.
        
        Args:
            index (int): The index of the token to retrieve.
        """
        
        return self.tokens[index]
        
    def __str__(self) -> str:
        """
        Print the document in a readable format.
        """
        
        tokens_str = "\n".join([str(token) for token in self.tokens])
        relations_str = "\n".join([str(relation) for relation in self.relations])
        
        return f"Document ID: {self.id}\nPath: {self.path}\nText: {self.text}\nTokens:\n{tokens_str}\nRelations:\n{relations_str}"