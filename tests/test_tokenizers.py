import unittest
from parselt.loaders import BratLoader, JSONLoader
from parselt import Document, Entity, Relation
from parselt.tokenizers import WordTokenizer
from intervaltree import Interval, IntervalTree

class WordTokenizerTest(unittest.TestCase):
    def setUp(self):
        self.tokenizer = WordTokenizer()
        self.document = Document(
            id="sample1",
            path="tests/input/brat/joined/sample1.ann",
            text="Barack Obama was born in Hawaii and later became the President of the United States.",
            entities=IntervalTree(
                    [Interval(begin=0, end=12, data=Entity("Barack Obama", 0, 12, label="Person", entity_id=1)),
                    Interval(begin=25, end=31, data=Entity("Hawaii", 25, 31, label="Location", entity_id=2)),
                    Interval(begin=53, end=62, data=Entity("President", 53, 62, label="Title", entity_id=3)),
                    Interval(begin=70, end=85, data=Entity("United States", 70, 85, label="Location", entity_id=4))]),
            relations=[]
        )
        
    def test_tokenize(self):
        self.document.tokenize(self.tokenizer)
        self.assertTrue(self.document.is_tokenized)
        self.assertEqual(len(self.document.tokens), 15)
        self.assertEqual(self.document.tokens[0].text, "Barack")
        self.assertEqual(self.document.tokens[0].start, 0)
        self.assertEqual(self.document.tokens[0].end, 6)
        self.assertEqual(self.document.tokens[0].label, "Person")