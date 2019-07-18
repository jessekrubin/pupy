# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python
from contextlib import contextmanager
from datetime import datetime
from os import environ
from os import makedirs
from os import path
from shutil import rmtree
from tempfile import mkdtemp
from time import sleep
from typing import Optional
from weakref import finalize

from pupy.sh import cd
from pupy.sh import link_dirs
from pupy.sh import link_files
from pupy.sh import path2name
from pupy.sh import pwd
from pupy.sh import unlink_dirs
from pupy.sh import unlink_files


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


def environ_dict():
    return {k: environ[k] for k in environ}


class LinkedTmpDir(object):
    """ make a temp dir and have links."""

    def __init__(
        self,
        suffix=None,
        prefix=None,
        dir=None,
        mkdirs=None,
        lndirs=None,
        lnfiles=None,
        link_targets=None,
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


# from tempfile import TemporaryDirectory, _get_candidate_names, _sanitize_params, mkdtemp
# from pprint import pprint as pp
# from os import path, access, name, fsencode, W_OK, mkdir

# def _mkdtemp(suffix=None, prefix=None, dir=None):
#     """Better version of mkdtemp
#     """
#
#     prefix, suffix, dir, output_type = _sanitize_params(prefix, suffix, dir)
#
#     names = _get_candidate_names()
#     if output_type is bytes:
#         names = map(fsencode, names)
#     for seq in range(10000):
#         name = next(names)
#         file = path.join(dir, prefix + name + suffix)
#         try:
#             mkdir(file, 0o777)
#             # mkdir(file, 0o700)
#         except FileExistsError:
#             continue  # try again
#         except PermissionError:
#             # This exception is thrown when a directory with the chosen name
#             # already exists on windows.
#             if (name == 'nt' and path.isdir(dir) and
#                 access(dir, W_OK)):
#                 continue
#             else:
#                 raise
#         return file
#
#     raise FileExistsError("No usable temporary directory name found")


@contextmanager
def linked_tmp_dir(
    suffix=None, prefix=None, dir=None, mkdirs=[], lndirs=[], lnfiles=[]
):
    temp_dir = mkdtemp(suffix=suffix, prefix=prefix, dir=dir)
    lnfiles = [
        (path.join(temp_dir, _rel_link), target) for _rel_link, target in lnfiles
    ]
    lndirs = [(path.join(temp_dir, _rel_link), target) for _rel_link, target in lndirs]
    # print(mkdirs)
    _dirs2make = [
        path.join(temp_dir, e)
        for e in (
            dirpath if isinstance(dirpath, str) else path.join(*dirpath)
            for dirpath in mkdirs
        )
    ]
    _dirs2make.extend((path.split(link)[0] for link, target in lnfiles))
    _dirs2make.extend((path.split(link)[0] for link, target in lndirs))
    for dirpath_route in _dirs2make:
        # print("mkingdir", dirpath_route)
        makedirs(path.join(temp_dir, dirpath_route), exist_ok=True)

    link_files(lnfiles)
    link_dirs(lndirs)
    # from pupy.foreign import files_gen, dirs_gen
    # from pprint import pprint
    # pprint(list(files_gen(temp_dir)))
    # pprint(list(dirs_gen(temp_dir)))
    # try:
    #     lndirs = (
    #         (path.join(temp_dir, _rel_link), target) for _rel_link, target in lndirs
    #     )
    # except TypeError as e:
    #     pass
    try:
        yield temp_dir
    finally:
        try:
            unlink_files(lnfiles)
        except Exception as e:
            pass
        try:
            unlink_dirs(lndirs)
        except Exception as e:
            pass
        try:
            rmtree(temp_dir)
        except PermissionError:
            # sleep(3)
            # print(pwd())
            # print(temp_dir)
            cd("..")
            # print(pwd())
            rmtree(temp_dir)
