# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
import contextlib
import shutil
import tempfile
from datetime import datetime
from os import environ
from os import getcwd
from os import listdir
from os import makedirs
from os import path
from os import stat
from platform import system
from tempfile import mkdtemp
from typing import List
from typing import Optional
from typing import Tuple
from weakref import finalize

from pupy import lin
from pupy import win
import pupy._typing

_OS = system().lower()

def fmt_bytes(num: pupy._typing.Flint) -> str:
    """
    this function will convert bytes to MB.... GB... etc

    .. doctest:: python

        >>> fmt_bytes(100)
        '100.0 bytes'
        >>> fmt_bytes(1000)
        '1000.0 bytes'
        >>> fmt_bytes(10000)
        '9.8 KB'
        >>> fmt_bytes(100000)
        '97.7 KB'
        >>> fmt_bytes(1000000)
        '976.6 KB'
        >>> fmt_bytes(10000000)
        '9.5 MB'
        >>> fmt_bytes(100000000)
        '95.4 MB'
        >>> fmt_bytes(1000000000)
        '953.7 MB'
        >>> fmt_bytes(10000000000)
        '9.3 GB'
        >>> fmt_bytes(100000000000)
        '93.1 GB'
        >>> fmt_bytes(1000000000000)
        '931.3 GB'
        >>> fmt_bytes(10000000000000)
        '9.1 TB'
        >>> fmt_bytes(100000000000000)
        '90.9 TB'

    """
    for x in ["bytes", "KB", "MB", "GB", "TB"]:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def fmt_file_size(filepath: str) -> str:
    """
    this function will return the file size
    """
    if path.isfile(filepath):
        file_info = stat(filepath)
        return fmt_bytes(file_info.st_size)

def fmt_seconds(t1: float, t2: Optional[float] = None) -> str:
    """Formats time string

    Formats t1 if t2 is None as a string; Calculates the time and formats
    the time t2-t1 if t2 is not None.

    :param t1: time 1/initial in seconds
    :type t1: double
    :param t2: time 2 (Default value = None)
    :type t2: None or double
    :returns: formated string of the t1 - t2 or t1
    :rtype: str

    """
    if t2 is not None:
        return fmt_seconds((t2 - t1))
    elif t1 == 0.0:
        return "0 sec"
    elif t1 >= 1:
        return "%.3f sec" % t1
    elif 1 > t1 >= 0.001:
        return "%.3f ms" % ((10 ** 3) * t1)
    elif 0.001 > t1 >= 0.000001:
        return "%.3f μs" % ((10 ** 6) * t1)
    elif 0.000001 > t1 >= 0.000000001:
        return "%.3f ns" % ((10 ** 9) * t1)
    else:
        return fmt_seconds((t2 - t1))

def path2name(path_str: str) -> str:
    """Get the parent-directory for a file or directory path as a string

    :param path_str:
    :return: The parent directory as a string

    .. doctest:: python

        >>> from os import getcwd
        >>> path2name(getcwd()) in getcwd()
        True

    """
    return path.split(path.abspath(path_str))[-1]

def parent_dirpath(fdpath: str) -> str:
    """

    :param fdpath: file/dir-path as as string
    :return:

    .. doctest:: python

        >>> from os import path
        >>> parent_dirpath(path.abspath(__file__)) in path.abspath(__file__)
        True

    """
    return path.split(fdpath)[0]

def timestamp(ts: Optional[float] = None) -> str:
    """Time stamp string w/ format yyyymmdd-HHMMSS

    :return: timestamp string

    .. doctest:: python

        >>> from datetime import datetime
        >>> stamps = ['20190225-161151', '20190225-081151']
        >>> timestamp(1551111111.111111) in stamps
        True
        >>> datetime.now().strftime("%Y%m%d-%H%M%S") == timestamp()
        True

    """
    if ts is None:
        return datetime.now().strftime("%Y%m%d-%H%M%S")
    elif isinstance(ts, float):
        return datetime.fromtimestamp(ts).strftime("%Y%m%d-%H%M%S")
    elif isinstance(ts, datetime):
        return ts.strftime("%Y%m%d-%H%M%S")

def ls(dirpath=".", abs=False):
    if abs:
        return [path.join(dirpath, item) for item in listdir(dirpath)]
    return listdir(dirpath)

def ls_files(dirpath, abs=False):
    files = (file for file in ls(dirpath, abs=True) if path.isfile(file))
    if not abs:
        return list(map(lambda el: el.replace(dirpath, "."), files))
    return list(files)

def ls_dirs(dirpath: str = ".", abs: bool = False):
    dirs = (dir for dir in ls(dirpath, abs=True) if path.isdir(dir))
    if not abs:
        return list(map(lambda el: el.replace(dirpath, "."), dirs))
    return list(dirs)

def ls_files_dirs(dirpath: str) -> Tuple[List[str], List[str]]:
    return ls_files(dirpath), ls_dirs(dirpath)

def link_dir(link, target):
    _link = win.link_dir if "win" in _OS else lin.link_dir
    return _link(link, target)

def link_dirs(link_target_tuples):
    _link = win.link_dirs if "win" in _OS else lin.link_dirs
    return _link(link_target_tuples)

def link_file(link, target):
    _link = win.link_file if "win" in _OS else lin.link_file
    makedirs(parent_dirpath(link), exist_ok=True)
    return _link(link, target)

def link_files(link_target_tuples):
    _link = win.link_files if "win" in _OS else lin.link_files
    link_target_tuples = list(link_target_tuples)
    for link, target in link_target_tuples:
        makedirs(parent_dirpath(link), exist_ok=True)
        print(link, parent_dirpath(link))
        print(path.exists(parent_dirpath(link)))
    _link(link_target_tuples)
    for link, target in link_target_tuples:
        makedirs(parent_dirpath(link), exist_ok=True)
        print(link, parent_dirpath(link))
        print(path.exists(link), path.exists(parent_dirpath(link)))

def unlink_dir(link_path: str):
    _unlink = win.unlink_dir if "win" in _OS else lin.unlink_dir
    return _unlink(link_path)

def unlink_dirs(link_paths):
    try:
        _unlink = win.unlink_dirs if "win" in _OS else lin.unlink_dirs
        return _unlink(link_paths)
    except TypeError:
        pass

def unlink_file(link):
    _unlink = win.unlink_file if "win" in _OS else lin.unlink_file
    return _unlink(link)

def unlink_files(links):
    try:
        _unlink = win.unlink_files if "win" in _OS else lin.unlink_files
        return _unlink(links)
    except TypeError:
        pass

def sync(src, dest):
    """Update (rsync/robocopy) a local test directory from raid

    :param dest: path to local tdir
    :param src: path to remote tdir
    :return: subprocess return code for rsync/robocopy
    """
    _sync = win.robocopy if "win" in _OS else lin.rsync
    return _sync(src=src, dest=dest)

def environ_dict():
    return {k: environ[k] for k in environ}

class LinkedTmpDir(object):
    """ make a temp dir and have links."""

    def __init__(self, suffix=None, prefix=None, dir=None,
                 mkdirs=None,
                 lndirs=None,
                 lnfiles=None,
                 link_targets=None
                 ):
        self.dirpath = mkdtemp(suffix, prefix, dir)
        self.dirname = path.split(self.dirpath)[-1]
        file_targets = []
        dir_targets = []
        if link_targets is None:
            link_targets = []
        for target in link_targets:
            if path.isfile(target):
                file_targets.append(target)
            elif path.isdir(target):
                dir_targets.append(target)
        _rel_file_links = list(map(path2name, file_targets))
        _rel_dir_links = list(map(path2name, dir_targets))

        try:
            assert len(set(_rel_file_links)) == len(_rel_file_links)
        except AssertionError as e:
            raise ValueError("Duplicate filenames present")
        try:
            assert len(set(_rel_dir_links)) == len(_rel_dir_links)
        except AssertionError as e:
            raise ValueError("Duplicate dirnames present")
        _lnk_path = lambda _lnk: path.join(self.dirpath, _lnk)
        self.file_links = list(map(_lnk_path, _rel_file_links))
        self.dir_links = list(map(_lnk_path, _rel_dir_links))
        link_files(zip(self.file_links, file_targets))
        link_dirs(zip(self.dir_links, dir_targets))
        self._finalizer = finalize(
            self,
            self._cleanup,
            self.dirpath,
            warn_message="Implicitly cleaning up {!r}".format(self),
            )

    @classmethod
    def _cleanup(cls, name, warn_message):
        pass

    def __repr__(self):
        return "<{} {!r}>".format(self.__class__.__name__, self.dirpath)

    def __enter__(self):
        return self.dirpath

    def __exit__(self, exc, value, tb):
        self.cleanup()

    def cleanup(self):
        unlink_dirs(self.dir_links)
        unlink_files(self.file_links)
        if self._finalizer.detach():
            pass

@contextlib.contextmanager
def linked_tmp_dir(suffix=None, prefix=None, dir=None,
                   mkdirs=None, lndirs=None, lnfiles=None):
    temp_dir = tempfile.mkdtemp(suffix=suffix, prefix=prefix, dir=dir)
    try:
        for dirpath_route in mkdirs:
            _abs_dirpath = path.join(temp_dir,
                                     dirpath_route if isinstance(dirpath_route, str) else path.join(*dirpath_route))
            makedirs(_abs_dirpath, exist_ok=True)
    except TypeError as e:
        pass

    try:
        lnfiles = ((path.join(temp_dir, _rel_link), target)
                   for _rel_link, target in lnfiles)
        link_files(lnfiles)
    except TypeError as e:
        pass
    try:
        lndirs = ((path.join(temp_dir, _rel_link), target)
                  for _rel_link, target in lndirs)
        link_dirs(lndirs)
    except TypeError as e:
        pass
    try:
        yield temp_dir
    finally:
        pass
        unlink_files(lnfiles)
        unlink_dirs(lndirs)
        shutil.rmtree(temp_dir)
