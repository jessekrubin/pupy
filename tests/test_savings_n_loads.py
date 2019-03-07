# -*- coding: utf-8 -*-
from os import path
from os import remove
from os import sep
from shutil import rmtree

import pytest

from pupy.savings_n_loads import ljasm
from pupy.savings_n_loads import ljson
from pupy.savings_n_loads import load_jasm
from pupy.savings_n_loads import lpak
from pupy.savings_n_loads import save_jasm
from pupy.savings_n_loads import sjasm
from pupy.savings_n_loads import sjson
from pupy.savings_n_loads import spak
from pupy.savings_n_loads import touch
from pupy.utils import parent_path

JASM_DICT = {"Jason": ["Green", "Berg"], "Jasm": ["Grundle", "Bug"]}


@pytest.mark.parametrize(
    "save_funk,load_funk",
    [[save_jasm, load_jasm], [sjson, ljson], [sjasm, ljasm], [spak, lpak]],
)
def test_ljson_n_sjson(save_funk: callable, load_funk: callable):
    """

    """
    save_funk("jasm_dict.json", JASM_DICT)
    loaded_data = load_funk("jasm_dict.json")
    assert loaded_data == JASM_DICT
    remove("jasm_dict.json")


@pytest.mark.parametrize(
    "fdpath",
    [
        "file.txt",
        path.join("dir", "file.txt"),
        path.join("dir1", "dir2", "file.txt"),
        path.join("dir1", "dir2", "dir3", "file.txt"),
        path.join("dir1", "dir2", "dir3", "dir4", "file.txt"),
    ],
)
def test_touch(fdpath):
    assert not path.exists(fdpath)
    touch(fdpath)
    assert path.exists(fdpath)

    root = fdpath.split(sep)[0]
    if path.isdir(root):
        rmtree(root)
    elif path.isfile(root):
        remove(root)
