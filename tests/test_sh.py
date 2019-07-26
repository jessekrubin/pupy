# -*- coding: utf-8 -*-
from os import mkdir
from os import path
from os import sep
from shutil import rmtree

from pupy.foreign import dirs_gen
from pupy.foreign import files_gen
from pupy.foreign import walk_gen
from pupy.savings_n_loads import touch
from pupy.sh import cd
from pupy.sh import mv


def test_mv_uno(tmpdir):
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
        filepath = path.join(tmpdir, *f)
        touch(filepath)
    files = list(sorted(files_gen(tmpdir)))
    print(files)
    cd(tmpdir)
    mkdir("out")
    mv("dir", "out")
    files = list(
        sorted((e.replace(str(tmpdir), "").strip(sep) for e in files_gen(tmpdir)))
    )
    print(files)

    expected = set(path.join("out", *f) for f in filepath_parts)
    got = set(files)
    assert expected == got


def test_mv_multi(tmpdir):
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
        filepath = path.join(tmpdir, *f)
        touch(filepath)
    files = list(sorted(files_gen(tmpdir)))
    # print(files)
    cd(tmpdir)
    mkdir("out")
    mv("dir/*", "out")
    files = list(
        sorted((e.replace(str(tmpdir), "").strip(sep) for e in files_gen(tmpdir)))
    )
    # print(files)
    expected = set(
        path.join("out", *f).replace(sep + "dir" + sep, "/") for f in filepath_parts
    )
    got = set(files)
    # print(expected)
    # print(got)
    assert expected == got
