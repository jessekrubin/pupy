# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from codecs import getwriter
from io import open
from itertools import count
from os import path
from os import utime
from typing import Dict
from typing import List

from pupy.decorations import mkdirs

try:
    from ujson import dump
    from ujson import load
except:
    from json import dump
    from json import load


def safepath(path_str: str) -> str:
    """Checks if a file/dir path is save/unused; returns an unused path.

    :param path_str: file or dir path
    :return: A file/dir path that does not exist and contains the given path

    """
    if path.exists(path_str):
        f_bn, f_ext = path.splitext(path_str)
        for n in count(1):
            safe_save_path = f_bn + "_({}).".format(str(n)) + f_ext
            if not path.exists(safe_save_path):
                return safe_save_path
    return path_str


def lbytes(filepath: str) -> None:
    """Read bytes from file path

    :param filepath: filepath as as string to read bites from
    :return: some bytes...
    """
    with open(filepath, "rb") as file:
        return file.read()


@mkdirs
def sstring(filepath: str, string: str) -> None:
    """Writes a string to filepath


    :param filepath: Filepath save location
    :param string: File as a string to be saved
    :return: None? what do you want? confirmation?

    .. note:: Decorated w/ @mkdirs
        Function is decorated with @mkdirs decorator; @mkdirs creates parent
        directories for the given filepath if they do not already exist.

    """
    with open(filepath, "wb") as file:
        file.write(string.encode("utf-8"))


def savings(filepath: str, string: str) -> None:
    """Alias for sstring"""
    return sstring(filepath, string)


def sstr(filepath: str, string: str) -> None:
    """Alias for sstring"""
    return sstring(filepath, string)


def lstring(filepath: str):
    """(lstring) Read and return the file-contents as a string given a filepath

    :param filepath: Path to a file to read
    :return: Content of the file read as a string

    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(filepath, "r", encoding="latin2") as f:
            return f.read()


def lstr(filepath):
    """Alias for lstring"""
    return lstring(filepath)


@mkdirs
def sjson(filepath: str, data: Dict[str, List[str]], min: bool = False) -> None:
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


def save_jasm(filepath: str, data: Dict[str, List[str]], min: bool = False) -> None:
    """Alias for sjson (which stands for 'save-json')"""
    return sjson(filepath, data, min)


def sjasm(filepath: str, data: Dict[str, List[str]], min: bool = False) -> None:
    """Alias for sjson (which stands for 'save-json')"""
    return sjson(filepath, data, min)


def spak(filepath: str, data: Dict[str, List[str]], min: bool = False) -> None:
    """Alias for sjson (which stands for 'save-json')"""
    return sjson(filepath, data, min)


@mkdirs
def ljson(filepath: str):
    """Load a json file given a filepath and return the file-data

    :param filepath: path to the jasm file you want to load
    :return: Loaded file contents
    """

    with open(filepath) as infile:
        return load(infile)


def load_jasm(filepath: str) -> Dict[str, List[str]]:
    """Alias for ljson (which stands for 'load-json')"""
    return ljson(filepath)


def ljasm(filepath: str) -> Dict[str, List[str]]:
    """Alias for ljson (which stands for 'load-json')"""
    return ljson(filepath)


def lpak(filepath: str) -> Dict[str, List[str]]:
    """Alias for ljson (which stands for 'load-json')"""
    return ljson(filepath)


@mkdirs
def touch(filepath: str) -> None:
    """Touches a file just like touch on the command line

    :param filepath: filepath to 'touch' in a unix-y sense
    :return: None
    """
    with open(filepath, "a"):
        utime(filepath, None)


def shebang(filepath: str):
    """returns the shebang path given a filepath or None if it does not exist.

    :param filepath: path to a file w/ a shebange line
    :return: shebang line or None

    .. doctest::python

        >>> from inspect import getabsfile
        >>> from pupy.savings_n_loads import sstr
        >>> script = 'ashellscript.sh'
        >>> sstr(script, '#!/bin/bash\\necho "howdy"\\n')
        >>> shebang(script)
        '#!/bin/bash'
        >>> from os import remove
        >>> remove(script)

    """
    with open(filepath, "r") as f:
        first = f.readline().strip("\n")
        return first if first[:2] == "#!" else None
