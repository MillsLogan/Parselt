from parselt.loaders import BratLoader, JSONLoader
from parselt.tokenizers import WordTokenizer

loader = BratLoader()
for doc in loader.load_directory("input/train"):
    print(doc)

