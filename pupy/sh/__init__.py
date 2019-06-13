# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from os import chdir
from os import getcwd
from os import lchmod
from os import listdir
from os import lstat
from os import makedirs
from os import path
from os import readlink
from os import remove
from os import rename
from os import stat
from os import symlink
from shutil import copy2
from shutil import copystat
from shutil import rmtree

mv = rename
pwd = getcwd
ls = listdir
cd = chdir


def cp(src, dst, r=False, symlinks=False, ignore=None):
    makedirs(dst, exist_ok=True)
    if not path.exists(dst):
        makedirs(dst, exist_ok=True)
        copystat(src, dst)
    _listdir = listdir(src)
    if ignore:
        _listdir = [x for x in _listdir if x not in set(ignore(src, _listdir))]
    for item in _listdir:
        _src_pth = path.join(src, item)
        _dest_pth = path.join(dst, item)
        if symlinks and path.islink(_src_pth):
            if path.lexists(_dest_pth):
                remove(_dest_pth)
            symlink(readlink(_src_pth), _dest_pth)
            try:
                st = lstat(_src_pth)
                mode = stat.S_IMODE(st.st_mode)
                lchmod(_dest_pth, mode)
            except:
                pass
        elif path.isdir(_src_pth):
            if r:
                cp(_src_pth, _dest_pth, r=True, symlinks=symlinks, ignore=ignore)
            else:
                print('{} is dir; use rm(..., r=True)'.format(_src_pth))
        else:
            copy2(_src_pth, _dest_pth)


def ls(dirpath=".", abs=False):
    if abs:
        return [path.join(dirpath, item) for item in listdir(dirpath)]
    return listdir(dirpath)


def rm(*args, r=False):
    for _path_str in args:
        if path.isfile(_path_str):
            remove(_path_str)
        elif path.isdir(_path_str):
            if r:
                rmtree(_path_str)
            else:
                print('{} is dir; use rm(..., r=True)'.format(_path_str))
