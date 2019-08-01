# -*- coding: utf-8 -*-
from os import path
from shutil import rmtree

from pupy.foreign import dirs_gen
from pupy.foreign import files_gen
from pupy.foreign import walk_gen, files_dirs_gen
from pupy.savings_n_loads import touch


def test_files_gen():
    filepath_parts = [
        ("dir", "file1.txt"),
        ("dir", "file2.txt"),
        ("dir", "file3.txt"),
        ("dir", "dir2", "file1.txt"),
        ("dir", "dir2", "file2.txt"),
        ("dir", "dir2", "file3.txt"),
        ("dir", "dir2a", "file1.txt"),
        ("dir", "dir2a", "file2.txt"),
        ("dir", "dir2a", "file3.txt"),
    ]
    for f in filepath_parts:
        filepath = path.join(*f)
        touch(filepath)
    expected_files = sorted(path.join(*f) for f in filepath_parts)
    files = list(sorted(files_gen("dir")))
    assert expected_files == files
    expected_dirs = sorted(
        set(
            path.join(*(part for part in f if ".txt" not in part))
            for f in filepath_parts
        )
    )
    dirs = list(sorted(dirs_gen("dir")))
    assert expected_dirs == dirs
    files_and_dirs = list(sorted(walk_gen("dir")))
    expected = set(expected_dirs + expected_files)
    got = set(files_and_dirs)
    print(expected, got)
    assert set(expected_dirs + expected_files) == set(files_and_dirs)
    rmtree("dir")


def test_files_n_dirs_gen():
    filepath_parts = [
        ("dir", "file1.txt"),
        ("dir", "file2.txt"),
        ("dir", "file3.txt"),
        ("dir", "dir2", "file1.txt"),
        ("dir", "dir2", "file2.txt"),
        ("dir", "dir2", "file3.txt"),
        ("dir", "dir2a", "file1.txt"),
        ("dir", "dir2a", "file2.txt"),
        ("dir", "dir2a", "file3.txt"),
    ]
    for f in filepath_parts:
        filepath = path.join(*f)
        touch(filepath)
    expected_files = sorted(path.join(*f) for f in filepath_parts)
    files, dirs = files_dirs_gen("dir")
    files_n_dirs = set(list(files) + list(dirs))
    walk_files_n_dirs = set(walk_gen("dir"))
    assert files_n_dirs == walk_files_n_dirs
