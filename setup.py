# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import setup, find_packages

# from Cython.Build import cythonize
# from sys import argv
#
# setup(name='pyEuler',
#       packages=['pupy'],
#       author='jessekrubin',
#       author_email='jessekrubin@gmail.com',
#       description='Pretty_Useful_Python',
#       requires=['tqdm', 'cython'])

# with open("README.md", "r") as fh:
#     long_description = fh.read()

# setup(
#     name="pupy",
#     version="1.0.4",
#     author="jessekrubin",
#     author_email="jessekrubin@gmail.com",
#     description="pretty useful python",
#     long_description="PUP",
#     long_description_content_type="text/markdown",
#     url="https://github.com/jessekrubin/pup",
#     # url='https://upload.pypi.org/legacy/',
#     packages=['pupy', 'test_pupy'],
#     classifiers=(
#         # "Programming Language :: Python :: 3",
#         # "License :: OSI Approved :: MIT License",
#         # "Operating System :: OS Independent",
#     ),
#     requires=['tqdm'],
#     python_requires='>=3'
# )
from setuptools import setup, find_packages
setup(
    name="pupy",
    version="1.0.6",
    packages=find_packages('pupy'),
    # scripts=['pu.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['tqdm>=4'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        # '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="jessekrubin",
    author_email="jessekrubin@gmail.com",
    description="This is a package",
    license="MIT",
    keywords="pretty useful python",
    url="http://github.com/jessekrubin/pupy/",   # project home page, if any
    project_urls={
        # "Documentation": "https://github.com/HelloWorld/",
        # "Source Code": "https://github.example.com/HelloWorld/",
    }

    # could also include long_description, download_url, classifiers, etc.
)

