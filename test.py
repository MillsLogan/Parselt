from ann_reader import AnnLoader

ann_reader = AnnLoader()
ann_reader("input/test/txts", "input/test/anns")
doc = next(iter(ann_reader.documents))

print(doc.as_entity_list())