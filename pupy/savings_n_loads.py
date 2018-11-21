#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from __future__ import with_statement, print_function
from os import path
from io import open
from json import load, dump
from codecs import getwriter
from itertools import count


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
    with open(safe_path(filepath) if safe_save else filepath, 'wb') as file:
        file.write(string.encode('utf-8'))


def loads(filepath):
    """Load a (txt) file as a string

    :param filepath: return:

    """
    if path.exists(filepath):
        with open(filepath, encoding='utf-8') as file:
            return file.read()
    else:
        raise FileNotFoundError("FILE NOT FOUND: {}".format(filepath))


def save_jasm(filepath, data, safe_save=False):
    """Save a python object as json file

    :param filepath: path w/ which 2 save the file
    :param data: some python text object that is hashable
    :param safe_save: return: None (Default value = False)
    :returns: None
    :rtype: None

    """

    with open(safe_path(filepath) if safe_save else filepath, 'wb') as file:
        dump(data, getwriter('utf-8')(file),
             indent=4,
             sort_keys=True,
             ensure_ascii=False)


def load_jasm(filepath):
    """

    :param filepath: path to the jasm (Jason Greenberg) file you want to load

    """
    with open(filepath) as infile:
        return load(infile)
