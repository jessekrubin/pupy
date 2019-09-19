# -*- coding: utf-8 -*-
import os
from os import mkdir
from os import path
from os import sep

from pupy.foreign import files_gen
from pupy.sh import cd
from pupy.sh import export
from pupy.sh import mv
from pupy.sh import rm
from pupy.sh import touch
from pupy.sh import tree

PWD = path.split(path.realpath(__file__))[0]

expected_dummy_dir_tree_full = """
dummy_dir/
├── a_dir/
│   ├── a_a_dir/
│   │   └── d_file.txt
│   └── c_file.txt
├── a_file.txt
├── b_dir/
│   ├── e_file.txt
│   └── f_file.txt
└── b_file.txt
"""


def test_tree():
    tree_string = tree(path.join(PWD, "dummy_dir"))
    print(tree_string)
    assert tree_string.strip("\n") == expected_dummy_dir_tree_full.strip("\n")


expected_dummy_dir_tree_keep_a_dir = """
dummy_dir/
└── a_dir/
    ├── a_a_dir/
    │   └── d_file.txt
    └── c_file.txt
"""


def test_tree_keep_a_dir():
    _ignore_funk = lambda s: "a_dir" in s
    tree_string = tree(path.join(PWD, "dummy_dir"), criteria=_ignore_funk)
    print(tree_string)
    assert tree_string.strip("\n") == expected_dummy_dir_tree_keep_a_dir.strip("\n")


expected_dummy_dir_tree_ignore_a_dir = """
dummy_dir/
├── a_file.txt
├── b_dir/
│   ├── e_file.txt
│   └── f_file.txt
└── b_file.txt
"""


def test_tree_ignore_a_dir():
    _ignore_funk = lambda s: "a_dir" not in s
    tree_string = tree(path.join(PWD, "dummy_dir"), criteria=_ignore_funk)
    print(tree_string)
    assert tree_string.strip("\n") == expected_dummy_dir_tree_ignore_a_dir.strip("\n")
