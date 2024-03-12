from setuptools import setup, find_packages

setup(name='ann_reader',
      version='1.0',
      description='A package for reading and working with .ann files',
      author='Logan Mills',
      url='github.com/millslogan/ann_reader',
      packages=['ann_reader', 'ann_reader.base_classes'],
      py_modules=['ann_loader', 'ann_reader.base_classes.document', 'validator'],
      python_requires='>=3.12'
)



