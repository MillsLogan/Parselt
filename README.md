# Parselt
Parselt is a flexible and extensible library designed for efficient document processing in NLP tasks. It provides tools for loading, tokenizing, and working with various document formats, such as BRAT and JSON annotations. With support for different tokenization strategies and easy integration into NLP pipelines, Parselt is a foundation for building robust text-processing workflows.

## Table of Contents
- [Parselt](#parselt)
  - [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
  - [Loading documents](#loading-documents)
  - [Tokenizing Loaded Documents](#tokenizing-loaded-documents)
- [Features](#features)

# Installation
To install parslet using pip:
```bash
pip install parselt
```
# Usage
## Loading documents
```python
from parselt.loaders import BratLoader

loader = BratLoader()
document = loader.load("path/to/document.ann")
```

## Tokenizing Loaded Documents
After loading a document, it's generally required to tokenize the text into encodable pieces. Parselt provides built-in tokenizers as well as an abstract class for users to extend and implement custom functionality.

Here's how we would tokenize a loaded document based on words, and punctuation:
```python
from parselt.tokenizers import WordTokenizer
tokenizer = WordTokenizer()
# document.text: "The quick brown fox (and so on)"
# document.tokens: []
document.tokenize(tokenizer)
# document.tokens: [Token(The, 0, 3, " "), Token(quick, 4, 9, " "), ..., Token(fox, 16, 19, " ("), ...]
```
This tokenizes the document in place, filling the `document.tokens` attribute with the resulting `Token` objects.

# Features
- Supports multiple document formats (BRAT, JSON)
- Flexible tokenization (word, sentence, and more)
- Easy extension for custom loaders and tokenizers

