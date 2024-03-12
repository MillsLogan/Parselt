from ann_reader.base_classes.loader import Loader
from ann_reader.base_classes.document import Document
from ann_reader.base_classes.entity import Entity
import os


class AnnLoader(Loader):
    '''
    Concrete implementation of the Loader class for loading
    documents and their corresponding annotation files into
    a dataset. All documents are stored in a dictionary with the document
    path as the key and the Document object as the value.
    You can load a single document or a directory of documents
    into the dataset, and iterate over the loader object to
    access the documents. When iterating over the loader object,
    only the document objects are returned, not the keys, if you
    want to access the keys (document path) use document.path.
    '''
    
    def __init__(self):
        '''
        Initialize the AnnLoader object.
        Note: The AnnLoader object is a subclass of the Loader class.
        Takes no arguments.
        '''
        super().__init__()
    
    def load(self, document_path: str, annotation_path: str = None) -> Document:
        '''
        Load a document and its corresponding annotation file into 
        a Document object and add it to the dataset.
        Takes two arguments:
        - document_path: str, the path to the document file.
        - annotation_path: str, the path to the annotation file. If None,
            the annotation file is assumed to have the same name as the
            document file, but with the .ann extension.
        '''
        
        if annotation_path is None:
            annotation_path = document_path.replace('.txt', '.ann')
        
        self.dataset[document_path] = self._create_document(document_path, annotation_path)
        return self.dataset[document_path]
    
    def load_all(self, document_dir: str, annotation_dir: str = None) -> list[Document]:
        '''
        Loads a directory of docuemtns and their corresponding annotation files
        into the dataset.
        Takes two arguments:
        - document_dir: str, the path to the directory containing the document files.
        - annotation_dir: str, the path to the directory containing the annotation files.
            If None, the annotation files are assumed to be in the same directory as
            the document files.
        '''
        loaded_documents = []
        if annotation_dir is None:
            annotation_dir = document_dir
        
        for document_path in os.listdir(document_dir):
            if document_path.endswith('.txt'):
                annotation_path = document_path.replace('.txt', '.ann')
                loaded_documents.append(self.load(os.path.join(document_dir, document_path), os.path.join(annotation_dir, annotation_path)))
        return loaded_documents
                
    def _create_document(self, document_path: str, annotation_path: str) -> Document:
        '''
        Protected method Please use the load method to create a Document object.
        
        Create a Document object from a document file and its corresponding
        annotation file.
        Takes two arguments:
        - document_path: str, the path to the document file.
        - annotation_path: str, the path to the annotation file.
        '''
        with open(document_path, 'r') as f:
            text = f.read()
            
        document = Document(document_path, text)
        
        with open(annotation_path, 'r') as f:
            for line in f:
                if line.startswith('T'):
                    entity = self._create_entity(line)
                    document.entities.append(entity)
                elif line.startswith('R'):
                    relation = self.create_relation(line)
                    document.relations.append(relation)
        
        return document
                    
    def _create_entity(self, line: str) -> Entity:
        '''
        Protected method. Please use see the load method to create a Document object.
        
        Create an Entity object from a line in an annotation file.
        Takes one argument:
        - line: str, a line from an annotation file.
        '''
        id, type_start_end, text = line.split('\t')
        id = int(id[1:])
        type, start, end = type_start_end.split(' ')
        start, end = int(start), int(end)
        text = text.strip()
        return Entity(id, type, start, end, text)
    
    