# -*- coding: utf-8 -*-
from distutils.core import setup
# from Cython.Build import cythonize
# from sys import argv
#
# setup(name='pyEuler',
#       packages=['pupy'],
#       author='jessekrubin',
#       author_email='jessekrubin@gmail.com',
#       description='Pretty_Useful_Python',
#       requires=['tqdm', 'cython'])
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pupy",
    version="1.0.3",
    author="jessekrubin",
    author_email="author@example.com",
    description="pretty useful python",
    long_description="PUP",
    long_description_content_type="text/markdown",
    # url="https://github.com/jessekrubin/pup",
    url='https://upload.pypi.org/legacy/',

    packages=setuptools.find_packages(),
    classifiers=(
        # "Programming Language :: Python :: 3",
    ),
    requires=['tqdm'],
    python_requires='>=3'
)