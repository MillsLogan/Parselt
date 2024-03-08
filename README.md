# ann_reader

A Python program for reading in a processing `.ann` and `.txt` file pairs into Python objects to make processing data seamless. Files should be in [Brat Standoff Format](https://brat.nlplab.org/standoff.html).

# Usage

First, install the program using pip

```shell
pip install git+https://github.com/MillsLogan/ann_reader
```

Next, you'll want to create a `Loader` object, depending on what format your documents are in.

> [!IMPORTANT]
> Currently only `.ann` files are supported with plans to incorporate `JSON` and `XML` later.

```python
from ann_reader import AnnLoader
loader = AnnLoader()
```

Now we can simply call the loader object with the path to the corresponding txt and ann files we'd like to process

```python
loader("path/to/txt/file.txt", "path/to/ann/file.ann")
```

> [!NOTE]
> If the `.txt` and `.ann` file are in the same directory, leaving the `annotation_path` argument as `None` will default to changing the document extension like so
>
> ```python
> loader("path/to/txt/file.txt")
> ```
>
> The loader will open `path/to/txt/file.txt` and `path/to/txt/file.ann`

All documents the loader processes are stored as key-value pairs where the document name is the key and the corresponding `Document` object is the value.

# Objects
## Document
The Document object is the encapsulation of the text of the sentence or document and the corresponding entities and relationships that exist within the text. 
### Fields
```python
class Document:
    # The path to the file
    path: str 

    # The raw text from the file
    text: str 
    
    # The entities from the annotation file wrapped in Entity objects stored in a list
    entities: list[Entity] 

    # The Relationships from the annotation file wrapped in Relation obejcts stored in a list
    relations: list[Relation] 
```
