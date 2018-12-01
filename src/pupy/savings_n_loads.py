#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from __future__ import print_function
from __future__ import with_statement

from codecs import getwriter
from datetime import datetime
from io import open
from itertools import count
from json import dump
from json import load
from os import path


def safe_path(filepath):
    """

    :param filepath: 

    """
    if path.exists(filepath):
        f_bn, f_ext = path.splitext(filepath)
        for n in count(1):
            safe_save_path = f_bn + "_({}).".format(str(n)) + f_ext
            if not path.exists(safe_save_path):
                return safe_save_path
    return filepath

def savings(filepath, string, safe_save=False):
    """Save s(tring) to filepath as txt file

    :param filepath: param string:
    :param safe_save: return: (Default value = False)
    :param string: 

    """
    with open(safe_path(filepath) if safe_save else filepath, "wb") as file:
        file.write(string.encode("utf-8"))

def loads(filepath):
    """Load a (txt) file as a string

    :param filepath: return:

    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError as e:
        with open(filepath, "r", encoding="latin2") as f:
            return f.read()

def save_jasm(filepath, data, min=False):
    """Save json-serial-ize-able data to a specific filepath.

    :param filepath: save filepath
    :param data: json ready data
    :param min: minified format flag
    :return: None
    """
    if type(data) == dict and any(type(val) == bytes for val in data.values()):
        data = {k: str(v, encoding="utf-8") for k, v in data.items()}
    if min and ".min.json" not in filepath:
        filepath = filepath.replace(".json", ".min.json")
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

def load_jasm(filepath):
    """

    :param filepath: path to the jasm (Jason Greenberg) file you want to load

    """
    with open(filepath) as infile:
        return load(infile)

def timestamp():
    """Time stamp string w/ format yyyy-mm-ddTHH-MM-SS

    :return: timestamp string
    """
    """Time stamp string w/ format yyyy-mm-ddTHH-MM-SS"""
    return datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

if __name__ == "__main__":
    pass
