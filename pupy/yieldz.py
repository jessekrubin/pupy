# -*- coding: utf-8 -*-

from os import getcwd
from os import path
from os import sep
from os import walk


def files_gen(dirpath: str = getcwd(), abs=True):
    """Yields paths beneath dirpath param; dirpath defaults to os.getcwd()

    :param dirpath: Directory path to walking down/through.
    :param abs: Yield the absolute path
    :return:
    """
    return (
        fpath if abs else fpath.replace(dirpath, "").strip(sep)
        for fpath in (
            path.join(pwd, file) for pwd, dirs, files in walk(dirpath) for file in files
        )
    )

def dirs_gen(dirpath: str = getcwd(), abs=True):
    """Yields paths beneath dirpath param; dirpath defaults to os.getcwd()

    :param dirpath: Directory path to walking down/through.
    :param abs: Yield the absolute path
    :return:

    """
    return (
        fpath if abs else fpath.replace(dirpath, "").strip(sep)
        for fpath in (pwd for pwd, dirs, files in walk(dirpath))
    )
