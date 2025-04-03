from setuptools import setup, find_packages

setup(name='Parselt',
      version='0.2.1',
      description='A package for reading and working with .ann files',
      author='Logan Mills',
      url='github.com/millslogan/parselt',
      packages=find_packages(),
      py_modules=['parselt', 'parselt.core'],
      python_requires='>=3.12'
)



