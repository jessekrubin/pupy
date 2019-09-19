# -*- coding: utf-8 -*-
import os
from os import mkdir
from os import path
from os import sep

import pytest

from pupy import files_gen
from pupy.sh import cd
from pupy.sh import cp
from pupy.sh import export
from pupy.sh import mv
from pupy.sh import rm
from pupy.sh import touch

PWD = path.split(path.realpath(__file__))[0]


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
        path.join("out", *f).replace(sep + "dir" + sep, sep) for f in filepath_parts
    )
    got = set(files)
    # print(expected)
    # print(got)
    assert expected == got


def test_export_single_key():
    key = "HERM=pood"
    from os import environ

    assert "HERM" not in environ
    export(key)
    assert "HERM" in environ
    assert environ["HERM"] == "pood"
    del environ["HERM"]


def test_export_key_val():
    key, val = "HERM", "pood"
    from os import environ

    assert "HERM" not in environ
    export(key, val)
    assert "HERM" in environ


@pytest.fixture(
    params=[
        "file.txt",
        path.join("dir", "file.txt"),
        path.join("dir1", "dir2", "file.txt"),
        path.join("dir1", "dir2", "dir3", "file.txt"),
        path.join("dir1", "dir2", "dir3", "dir4", "file.txt"),
    ]
)
def dummy_filepath(request):
    return request.param


def test_touch(dummy_filepath, tmpdir):
    fdpath = path.join(tmpdir, dummy_filepath)
    assert not path.exists(fdpath)
    touch(fdpath)
    assert path.exists(fdpath)


def test_rm_multi(tmpdir):
    os.chdir(tmpdir)
    test_files = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "a", "s", "d"]
    mkdir("test_env")
    cd("test_env")
    test_files = [x + ".txt" for x in test_files]
    for x in test_files:
        with open(x, "w") as f:
            f.write(" ")
    expected = []
    cd(tmpdir)
    rm("test_env/*.txt")
    actual = os.listdir("test_env")
    assert expected == actual


def test_rm_para(tmpdir):
    os.chdir(tmpdir)
    test_files = ["q", "w", "e"]
    mkdir("test_env")
    cd("test_env")
    test_files = [x + ".txt" for x in test_files]
    for x in test_files:
        with open(x, "w") as f:
            f.write(" ")
    expected = []
    cd(tmpdir)
    actual = os.listdir("test_env")
    rm("test_env", r=True)
    assert not os.path.exists("test_env")


def test_cp(tmpdir):
    os.chdir(tmpdir)
    test_files = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "a", "s", "d"]
    mkdir("test_env")
    cd("test_env")
    test_files = [x + ".txt" for x in test_files]
    for x in test_files:
        with open(x, "w") as f:
            f.write(" ")
    cd(tmpdir)
    os.mkdir("cp_dir")
    print(os.listdir("."))
    cp("test_env/*.txt", "cp_dir")

    actual = os.listdir("cp_dir")
    assert set(test_files) == set(actual)


def test_cp_dir(tmpdir):
    os.chdir(tmpdir)
    test_files = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "a", "s", "d"]
    mkdir("test_env")
    cd("test_env")
    test_files = [x + ".txt" for x in test_files]
    for x in test_files:
        with open(x, "w") as f:
            f.write(" ")
    cd(tmpdir)
    print(os.listdir("."))
    cp("test_env", "cp_dir", r=True)
    actual = os.listdir("cp_dir")
    assert set(test_files) == set(actual)
