import unittest
from parselt.loaders import BratLoader, JSONLoader
from parselt import Document

class LoaderTestCase(unittest.TestCase):
    def helper_test_load_sample1(self, document: Document, directory: str = "tests/input/brat/joined", extension: str = ".ann"):
        self.assertNotEqual(document, None)
        self.assertEqual(document.id, "sample1")
        self.assertEqual(document.path, f"{directory}/sample1{extension}")
        self.assertEqual(document.text.strip(), "Barack Obama was born in Hawaii and later became the President of the United States.")
        self.assertEqual(len(document.entities), 4)
        self.assertEqual(len(document.relations), 0)
        
        for interval in document.entities:
            if interval.data.label == "Person":
                self.assertEqual(interval.data.text, "Barack Obama")
                self.assertEqual(interval.data.entity_id, 1)
            elif interval.data.label == "Location":
                self.assertIn(interval.data.text, ["Hawaii", "United States"])
                self.assertIn(interval.data.entity_id, [2, 4])
            elif interval.data.label == "Title":
                self.assertEqual(interval.data.text, "President")
                self.assertEqual(interval.data.entity_id, 3)
            elif interval.data.label == "Location":
                self.assertEqual(interval.data.text, "United States")
                self.assertEqual(interval.data.entity_id, 4)
        

    def helper_test_load_sample2(self, document: Document, directory: str = "tests/input/brat/joined", extension: str = ".ann"):
        self.assertNotEqual(document, None)
        self.assertEqual(document.id, "sample2")
        self.assertEqual(document.path, f"{directory}/sample2{extension}")
        self.assertEqual(document.text.strip(), "Elon Musk founded SpaceX in 2002. He is also the CEO of Tesla.")
        self.assertEqual(len(document.entities), 4)
        self.assertEqual(len(document.relations), 2)
        
        for interval in document.entities:
            if interval.data.label == "Person":
                self.assertEqual(interval.data.text, "Elon Musk")
                self.assertEqual(interval.data.entity_id, 1)
            elif interval.data.label == "Organization":
                self.assertIn(interval.data.text, ["SpaceX", "Tesla"])
                self.assertIn(interval.data.entity_id, [2, 3])
            elif interval.data.label == "Date":
                self.assertEqual(interval.data.text, "2002")
                self.assertEqual(interval.data.entity_id, 4)

class TestBratLoader(LoaderTestCase):
    def test_load_file_invalid_format(self):
        loader = BratLoader()
        document = loader.load_file("tests/input/brat/joined/sample1.txt")
        assert document is None

    def test_load_file_no_text_dir(self):
        loader = BratLoader()
        document = loader.load_file("tests/input/brat/joined/sample1.ann")
        self.helper_test_load_sample1(document)

    def test_load_file_with_text_dir(self):
        loader = BratLoader(text_dir="tests/input/brat/txts")
        document = loader.load_file("tests/input/brat/anns/sample1.ann")
        self.helper_test_load_sample1(document, directory="tests/input/brat/anns")

    def test_load_joint_directory(self):
        loader = BratLoader()
        documents = list(loader.load_directory("tests/input/brat/joined"))
        self.assertEqual(len(documents), 2)
        for document in documents:
            if document.id == "sample1":
                self.helper_test_load_sample1(document)
            elif document.id == "sample2":
                self.helper_test_load_sample2(document)
        
    def test_load_directory_with_text_dir(self):
        loader = BratLoader(text_dir="tests/input/brat/txts")
        documents = list(loader.load_directory("tests/input/brat/anns"))
        self.assertEqual(len(documents), 2)
        for document in documents:
            if document.id == "sample1":
                self.helper_test_load_sample1(document, directory="tests/input/brat/anns")
            elif document.id == "sample2":
                self.helper_test_load_sample2(document, directory="tests/input/brat/anns")

class JSON_Loader(LoaderTestCase):
    def test_json_load_sample1(self):
        loader = JSONLoader()
        document = loader.load_file("tests/input/json/sample1.json")
        self.helper_test_load_sample1(document, directory="tests/input/json", extension=".json")
        
    def test_json_load_sample2(self):
        loader = JSONLoader()
        document = loader.load_file("tests/input/json/sample2.json")
        self.helper_test_load_sample2(document, directory="tests/input/json", extension=".json")

if __name__ == "__main__":
    unittest.main()




