from parselt.loaders import BratLoader
from parselt.tokenizers import WordTokenizer

loader = BratLoader("input/test/txts")
for doc in loader.load_directory("input/test/anns"):
    doc.tokenize(WordTokenizer())
    print(doc)
    print(doc.text)
    print(doc.entities)
    print(doc.relations)
    print()
    for token in doc.tokens:
        print(token, token.start, token.end, token.next_char)
    exit()
