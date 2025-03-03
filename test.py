from parselt.loaders import BratLoader, JSONLoader
from parselt.tokenizers import WordTokenizer

loader = JSONLoader()
doc = loader.load_file("input/json_test.json")
print(doc[1])

