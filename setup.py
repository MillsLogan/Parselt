from setuptools import setup, find_packages

setup(name='Parselt',
      version='1.1',
      description='A package for reading and working with .ann files',
      author='Logan Mills',
      url='github.com/millslogan/parselt',
      packages=find_packages(),
      py_modules=['parselt', 'parselt.core', 'validator'],
      python_requires='>=3.12'
)



