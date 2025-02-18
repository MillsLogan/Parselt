from ann_reader import Document
from ann_reader.loaders import BratLoader

loader = BratLoader("input/test/txts")
for doc in loader.load_directory("input/test/anns"):
    print(doc)
    print(doc.text)
    print(doc.entities)
    print(doc.relations)
    print()
    exit()
