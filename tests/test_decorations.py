# -*- coding: utf-8 -*-
from os import path
from time import sleep

from pupy import sstring
from pupy.decorations import cprof
from pupy.decorations import dirdec
from pupy.decorations import tictoc


def test_mkdirs_dec(tmpdir):
    dirpath = path.join(tmpdir, "some_non_existing_dir")
    filepath = path.join(tmpdir, "some_non_existing_dir", "thisfilepath.txt")
    sstring(filepath, "12345432345432134")
    assert path.exists(filepath)
    assert path.exists(dirpath)
    assert path.isdir(dirpath)


def test_mkdirs_dec_kwargs(tmpdir):
    dirpath = path.join(tmpdir, "some_non_existing_dir")
    filepath = path.join(tmpdir, "some_non_existing_dir", "thisfilepath.txt")
    sstring(filepath=filepath, string="12345432345432134")
    assert path.exists(filepath)
    assert path.exists(dirpath)
    assert path.isdir(dirpath)


def test_dirdec(tmpdir):
    dirpath = path.join(tmpdir, "a_directory_name")

    @dirdec
    def _funk():
        return dirpath

    assert not path.exists(dirpath)
    assert not path.isdir(dirpath)
    _funk()
    assert path.exists(dirpath)
    assert path.isdir(dirpath)
    _funk()
    assert path.exists(dirpath)
    assert path.isdir(dirpath)


def test_tictoc(capfd):
    @tictoc()
    def _funk():
        sleep(1)

    _funk()
    out, err = capfd.readouterr()
    assert "_funk" in out
    assert "__TICTOC__" in out


def test_cprof(capfd):
    @cprof
    def _funk():
        sleep(1)

    _funk()
    out, err = capfd.readouterr()
    assert "__CPROFILE__" in out
    assert "3 function calls" in out
