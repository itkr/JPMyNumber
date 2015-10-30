import os

from setuptools import setup

from jpmynumber import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r') as f:
    long_description = f.read()


setup(
    name='JPMyNumber',
    version=__version__,
    author='itkr',
    author_email='itkrst@gmail.com',
    description=(
        'MyNumber (Japanese common number of social security and tax) library'),
    long_description=long_description,
    license='MIT',
    keywords=['MyNumber', 'Japanese'],
    url='https://github.com/itkr/JPMyNumber',
    packages=['jpmynumber'],
)
