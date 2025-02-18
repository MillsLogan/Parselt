from setuptools import setup, find_packages

setup(name='Parselt',
      version='1.0',
      description='A package for reading and working with .ann files',
      author='Logan Mills',
      url='github.com/millslogan/parselt',
      packages=['parselt', 'parselt.base_classes'],
      py_modules=['parselt', 'parselt.base_classes.document', 'validator'],
      python_requires='>=3.12'
)



