# -*- coding: utf-8 -*-

from os import path

from pupy.utils import pyfilepath


def test_pyfilepath_filepath():
    a = pyfilepath()
    assert a.endswith("test_utils.py")


def test_pyfilepath_split():
    filepath = pyfilepath()
    dirpath, filename = pyfilepath(split=True)
    assert path.join(dirpath, filename) == filepath
