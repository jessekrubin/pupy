# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from __future__ import print_function
from __future__ import with_statement

from codecs import getwriter
from io import open
from itertools import count
from os import path
from os import utime

from pupy.decorations import mkdirs

try:
    from ujson import dump
    from ujson import load
except Exception as e:
    from json import dump
    from json import load

def safepath(path_str):
    """Checks if a file/dir path is save/unused; returns an unused path.

    :param path_str:

    """
    if path.exists(path_str):
        f_bn, f_ext = path.splitext(path_str)
        for n in count(1):
            safe_save_path = f_bn + "_({}).".format(str(n)) + f_ext
            if not path.exists(safe_save_path):
                return safe_save_path
    return path_str

@mkdirs
def savings(filepath, string, clobber=True):
    """Writes a string to filepath


    :param filepath: Filepath save location
    :param string: File as a string to be saved
    :param clobber: Save over a file if the filepath exists
    :return: None? what do you want? confirmation?

    .. note:: Decorated w/ @mkdirs
        Function is decorated with @mkdirs decorator; @mkdirs creates parent
        directories for the given filepath if they do not already exist.

    """
    if not clobber and path.exists(filepath):
        filepath = safepath(filepath)
    with open(filepath, "wb") as file:
        file.write(string.encode("utf-8"))

def loads(filepath):
    """Read and return the file-contents as a string given a filepath

    :param filepath: Path to a file to read
    :return: Content of the file read as a string

    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError as e:
        with open(filepath, "r", encoding="latin2") as f:
            return f.read()

@mkdirs
def sjson(filepath, data, min=False):
    """Save json-serial-ize-able data to a specific filepath.

    :param filepath: destination filepath
    :param data: json cereal-izable dictionary/list/thing
    :param min: Bool flag -- minify the json file
    :return: None

    """
    if type(data) == dict and any(type(val) == bytes for val in data.values()):
        data = {k: str(v, encoding="utf-8") for k, v in data.items()}
    with open(filepath, "wb") as jsonfile:
        if min:
            dump(data, getwriter("utf-8")(jsonfile), ensure_ascii=False)
        else:
            dump(
                data,
                getwriter("utf-8")(jsonfile),
                indent=4,
                sort_keys=True,
                ensure_ascii=False,
                )

def save_jasm(filepath, data, min=False):
    """Alias for sjson (which stands for 'save-json')"""
    return sjson(filepath, data, min)

def sjasm(filepath, data, min=False):
    """Alias for sjson (which stands for 'save-json')"""
    return sjson(filepath, data, min)

def spak(filepath, data, min=False):
    """Alias for sjson (which stands for 'save-json')"""
    return sjson(filepath, data, min)

@mkdirs
def ljson(filepath):
    """Load a json file given a filepath and return the file-data

    :param filepath: path to the jasm file you want to load
    :return: Loaded file contents
    """

    with open(filepath) as infile:
        return load(infile)

def load_jasm(filepath):
    """Alias for ljson (which stands for 'load-json')"""
    return ljson(filepath)

def ljasm(filepath):
    """Alias for ljson (which stands for 'load-json')"""
    return ljson(filepath)

def lpak(filepath):
    """Alias for ljson (which stands for 'load-json')"""
    return ljson(filepath)

@mkdirs
def touch(filepath):
    """Touches a file just like touch on the command line

    :param filepath: filepath to 'touch' in a unix-y sense
    :return: None
    """
    with open(filepath, "a"):
        utime(filepath, None)
