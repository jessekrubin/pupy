# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python
"""
=========
Shell-ish
=========
"""
from distutils.dir_util import copy_tree
from functools import lru_cache
from glob import iglob
from io import open
from os import chdir
from os import environ
from os import getcwd
from os import listdir
from os import makedirs
from os import path
from os import remove
from os import symlink
from os import unlink
from os import utime
from pathlib import Path
from platform import system
from shutil import copy2
from shutil import move
from shutil import rmtree
from subprocess import PIPE
from subprocess import run
from typing import List
from typing import Tuple
from typing import Union

from pupy import mkdirs
from pupy.foreign import chunks


class LIN:
    @staticmethod
    def rsync_args(
        src, dest, delete=False, mkdirs=False, exclude=None, include=None, dry_run=False
    ):
        """Sheldon rsync wrapper for syncing tdirs

        Args:
          dest: path to local tdir
          src: path to remote (raid) tdir

        Returns:
          subprocess return code from rsync

          Rsync return codes:

          - 0 == Success
          - 1 == Syntax or usage error
          - 2 == Protocol incompatibility
          - 3 == Errors selecting input/output files, dirs
          - 4 == Requested  action not supported: an attempt was made to manipulate
          64-bit files on a platform that cannot support them; or an option
          was specified that is supported by the client and not the server.
          - 5 == Error starting client-server protocol
          - 6 == Daemon unable to append to log-file
          - 10 == Error in socket I/O
          - 11 == Error in file I/O
          - 12 == Error in rsync protocol data stream
          - 13 == Errors with program diagnostics
          - 14 == Error in IPC code
          - 20 == Received SIGUSR1 or SIGINT
          - 21 == Some error returned by waitpid()
          - 22 == Error allocating core memory buffers
          - 23 == Partial transfer due to error
          - 24 == Partial transfer due to vanished source files
          - 25 == The --max-delete limit stopped deletions
          - 30 == Timeout in data send2viewserver/receive
          - 35 == Timeout waiting for daemon connection
          :param src:
          :param dest:
          :param delete:
          :param mkdirs:
          :param exclude:
          :param include:
          :param dry_run:

        """
        if exclude is None:
            exclude = []
        if include is None:
            include = []
        if mkdirs:
            try:
                assert path.exists(dest) and path.isdir(dest)
            except AssertionError:
                makedirs(dest, exist_ok=True)

        if not dest.endswith("/"):
            dest = "{}/".format(dest)
        if not src.endswith("/"):
            src = "{}/".format(src)
        _args = [
            "rsync",
            "-a",
            "-O",
            "--no-o",
            "--no-g",
            "--no-p",
            "--delete" if delete else None,
            *('--exclude="{}"'.format(pattern) for pattern in exclude),
            *('--include="{}"'.format(pattern) for pattern in include),
            *(("--dry-run", "-i") if dry_run else (None,)),
            src,
            dest,
        ]
        return list(filter(None, _args))

    @staticmethod
    def rsync(src, dest, delete=False, exclude=None, include=None, dry_run=False):
        """Sheldon rsync wrapper for syncing tdirs

        :param exclude:
        :param include:
        :param dry_run:
        :param delete:
        :param dest: path to local tdir
        :param src: path to remote (raid) tdir
        :return: subprocess return code from rsync

        Rsync return codes:

         - 0 == Success
         - 1 == Syntax or usage error
         - 2 == Protocol incompatibility
         - 3 == Errors selecting input/output files, dirs
         - 4 == Requested  action not supported: an attempt was made to manipulate
           64-bit files on a platform that cannot support them; or an option
           was specified that is supported by the client and not the server.
         - 5 == Error starting client-server protocol
         - 6 == Daemon unable to append to log-file
         - 10 == Error in socket I/O
         - 11 == Error in file I/O
         - 12 == Error in rsync protocol data stream
         - 13 == Errors with program diagnostics
         - 14 == Error in IPC code
         - 20 == Received SIGUSR1 or SIGINT
         - 21 == Some error returned by waitpid()
         - 22 == Error allocating core memory buffers
         - 23 == Partial transfer due to error
         - 24 == Partial transfer due to vanished source files
         - 25 == The --max-delete limit stopped deletions
         - 30 == Timeout in data send2viewserver/receive
         - 35 == Timeout waiting for daemon connection

        """
        if exclude is None:
            exclude = []
        if include is None:
            include = []
        rsync_args = LIN.rsync_args(
            src,
            dest,
            delete=delete,
            mkdirs=True,
            exclude=exclude,
            include=include,
            dry_run=dry_run,
        )
        subproc = run(args=list(filter(None, rsync_args)), stdout=PIPE, stderr=PIPE)
        return subproc

    @staticmethod
    def link_dir(linkpath, targetpath):
        """

        :param linkpath:
        :param targetpath:
        """
        symlink(targetpath, linkpath)

    @staticmethod
    def link_dirs(link_target_tuples):
        """

        :param link_target_tuples:
        """
        for link, target in link_target_tuples:
            LIN.link_dir(link, target)

    @staticmethod
    def link_file(linkpath: str, targetpath: str) -> None:
        """

        :param linkpath:
        :param targetpath:
        """
        makedirs(path.split(linkpath)[0], exist_ok=True)
        symlink(targetpath, linkpath)

    @staticmethod
    def link_files(link_target_tuples):
        """

        :param link_target_tuples:
        """
        for link, target in link_target_tuples:
            LIN.link_file(link, target)

    @staticmethod
    def unlink_dir(link):
        """

        :param link:
        """
        unlink(link)

    @staticmethod
    def unlink_dirs(links):
        """

        :param links:
        """
        for link in links:
            unlink(link)

    @staticmethod
    def unlink_file(link):
        """

        :param link:
        """
        unlink(link)

    @staticmethod
    def unlink_files(links):
        """

        :param links:
        """
        for link in links:
            unlink(link)

    sync = rsync


@lru_cache(maxsize=None)
def _check_link_target_files(link, target):
    # for link, target in link_target_tuples:
    try:
        assert path.exists(target)
        makedirs(path.split(link)[0], exist_ok=True)
        # _exists.extend(["mklink", link, target, "&&"])
        return True
        # _exists.extend(["mklink", link, target, "&&"])
    except AssertionError as e:
        print(
            "Link target not found; unable to create link:\n    {} => {}".format(
                link, target
            )
        )
        print("Exception: " + str(e))
    except Exception as e:
        print(e, type(e))
    return False


@lru_cache(maxsize=None)
def _check_link_target_dirs(link, target):
    # for link, target in link_target_tuples:
    try:
        assert path.exists(target) and path.isdir(target)
        makedirs(path.split(link)[0], exist_ok=True)
        # _exists.extend(["mklink", link, target, "&&"])
        # _exists.extend(["mklink", link, target, "&&"])
    except AssertionError as e:
        print(
            "Link target not found; unable to create link:\n    {} => {}".format(
                link, target
            )
        )
        print("Exception: " + str(e))
        return False
    except Exception as e:
        print(e, type(e))
    return True


class WIN:

    # def rsync_args(src, dest,
    #                delete=False, mkdirs=False,
    #                exclude=[], include=[], dry_run=False):
    @staticmethod
    def robocopy_args(
        src, dest, delete=False, exclude_files=None, exclude_dirs=None, dry_run=False
    ):
        """Robocopy for sheldon

        Args:
          dest: path to local tdir
          src: path to remote (raid) tdir

        Returns:
          subprocess return code from robocopy

          Robocopy return codes:

          0. No files were copied. No failure was encountered. No files were
          mismatched. The files already exist in the destination directory;
          therefore, the copy operation was skipped.
          1. All files were copied successfully.
          2. There are some additional files in the destination directory that are not
          present in the source directory. No files were copied.
          3. Some files were copied. Additional files were present. No failure
          was encountered.
          5. Some files were copied. Some files were mismatched. No failure was
          encountered.
          6. Additional files and mismatched files exist. No files were copied
          and no failures were encountered. This means that the files already
          exist in the destination directory.
          7. Files were copied, a file mismatch was present, and additional files
          were present.
          8. Several files did not copy.
          :param src:
          :param dest:
          :param delete:
          :param exclude_files:
          :param exclude_dirs:
          :param dry_run:

        """
        if exclude_files is None:
            exclude_files = []
        if exclude_dirs is None:
            exclude_dirs = []
        _args = [
            "robocopy",
            src,
            dest,
            "/MIR" if delete else "/E",
            "/mt",
            "/W:1",
            "/R:1",
        ]
        if exclude_dirs:
            _args.extend(["/XD", *exclude_dirs])
        if exclude_files:
            _args.extend(["/XF", *exclude_files])
        if dry_run:
            _args.append("/L")
        return list(filter(None, _args))

    @staticmethod
    def robocopy(
        src, dest, delete=False, exclude_files=None, exclude_dirs=None, dry_run=False
    ):
        """Robocopy for sheldon

        :param delete:
        :param exclude_files:
        :param exclude_dirs:
        :param dry_run:
        :param dest: path to local tdir
        :param src: path to remote (raid) tdir
        :return: subprocess return code from robocopy

        Robocopy return codes:

        0. No files were copied. No failure was encountered. No files were
           mismatched. The files already exist in the destination directory;
           therefore, the copy operation was skipped.
        1. All files were copied successfully.
        2. There are some additional files in the destination directory that are not
           present in the source directory. No files were copied.
        3. Some files were copied. Additional files were present. No failure
           was encountered.
        5. Some files were copied. Some files were mismatched. No failure was
           encountered.
        6. Additional files and mismatched files exist. No files were copied
           and no failures were encountered. This means that the files already
           exist in the destination directory.
        7. Files were copied, a file mismatch was present, and additional files
           were present.
        8. Several files did not copy.


        """
        if exclude_files is None:
            exclude_files = []
        if exclude_dirs is None:
            exclude_dirs = []
        _args = WIN.robocopy_args(
            src=src,
            dest=dest,
            delete=delete,
            exclude_files=exclude_files,
            exclude_dirs=exclude_dirs,
            dry_run=dry_run,
        )
        subproc = run(args=_args, stdout=PIPE, stderr=PIPE)
        return subproc

    @staticmethod
    def link_dir(link, target):
        """

        :param link:
        :param target:
        """
        makedirs(link, exist_ok=True)
        run(args=["mklink", "/D", link, target], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def link_dirs(link_target_tuples):
        """

        :param link_target_tuples:
        """
        _exists = [
            "mklink /D {} {}".format(link, target)
            for link, target in link_target_tuples
            if _check_link_target_dirs(link, target)
        ]
        _proc = run(
            args=" && ".join(_exists).split(" "), stdout=PIPE, stderr=PIPE, shell=True
        )
        stderr = _proc.stderr.decode()
        if "too" in stderr and "long" in stderr:
            tuple_chunks = list(
                chunks(link_target_tuples, len(link_target_tuples) // 2)
            )
            for tuple_chunk in tuple_chunks:
                WIN.link_dirs(tuple_chunk)

    @staticmethod
    def link_file(link, target):
        """

        :param link:
        :param target:
        """
        makedirs(path.split(link)[0], exist_ok=True)
        run(args=["mklink", link, target], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def link_files(link_target_tuples):
        """

        :param link_target_tuples:
        """
        link_target_tuples = list(link_target_tuples)
        _exists = [
            "mklink {} {}".format(link, target)
            for link, target in link_target_tuples
            if _check_link_target_files(link, target)
        ]
        _proc = run(
            args=" && ".join(_exists).split(" "), stdout=PIPE, stderr=PIPE, shell=True
        )
        stdout = _proc.stdout.decode()
        stderr = _proc.stderr.decode()
        if ("too" in stderr and "long" in stderr) or (
            "too" in stderr and "long" in stdout
        ):
            tuple_chunks = list(
                chunks(link_target_tuples, len(link_target_tuples) // 2)
            )
            for tuple_chunk in tuple_chunks:
                WIN.link_files(tuple_chunk)

    @staticmethod
    def unlink_dir(link):
        """

        :param link:
        """
        run(args=["RD", link], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def unlink_dirs(links):
        """

        :param links:
        """
        cmd_args = " && ".join("RD {}".format(link) for link in links).split(" ")
        run(args=cmd_args, stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def unlink_file(link):
        """

        :param link:
        """
        run(args=["Del", link], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def unlink_files(links):
        """

        :param links:
        """
        cmd_args = " && ".join("Del {}".format(link) for link in links).split(" ")
        run(args=cmd_args, stdout=PIPE, stderr=PIPE, shell=True)

    sync = robocopy


class DirTree:
    """

    """

    _filename_prefix_mid: str = "├──"
    _filename_prefix_last: str = "└──"
    _parent_prefix_middle: str = "    "
    _parent_refix_last: str = "│   "

    def __init__(self, path: str, parent_path: str, is_last: bool):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        self.depth: int = self.parent.depth + 1 if self.parent else 0

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        """

        :param root:
        :param parent:
        :param is_last:
        :param criteria:
        """
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(
            list(path for path in root.iterdir() if criteria(str(path))),
            key=lambda s: str(s).lower(),
        )
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(
                    path, parent=displayable_root, is_last=is_last, criteria=criteria
                )
            else:
                # print(path)
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path_string):
        ignore_strings = (".pyc", "__pycache__")
        return not any(
            ignored in str(path_string).lower() for ignored in ignore_strings
        )

    @property
    def displayname(self):
        """

        :return:
        """
        if self.path.is_dir():
            return self.path.name + "/"
        return self.path.name

    def displayable(self):
        """

        :return:
        """
        if self.parent is None:
            return self.displayname

        _filename_prefix = (
            self._filename_prefix_last if self.is_last else self._filename_prefix_mid
        )

        parts = ["{!s} {!s}".format(_filename_prefix, self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(
                self._parent_prefix_middle
                if parent.is_last
                else self._parent_refix_last
            )
            parent = parent.parent

        return "".join(reversed(parts))


# _OS = system().lower()
_OS = WIN if "windows" in system().lower() else LIN

pwd = getcwd
cd = chdir


def tree(dirpath, criteria=None):
    """

    :param dirpath:
    :param criteria:
    :return:
    """
    return "\n".join(
        p.displayable() for p in DirTree.make_tree(Path(dirpath), criteria=criteria)
    )


def mv(src, dst):
    """

    :param src:
    :param dst:
    """
    for file in iglob(src, recursive=True):
        move(file, dst)


def cp_file(source: str, target: str) -> None:
    """

    :param source:
    :param target:
    """
    try:
        makedirs(path.dirname(target), exist_ok=True)
    except FileNotFoundError:
        pass
    copy2(source, target)


def cp_dir(source: str, target: str) -> None:
    """

    :param source:
    :param target:
    """
    if not path.exists(target):
        makedirs(target)
    copy_tree(source, target)


def cp(src: str, target: str, f: bool = True, r: bool = False) -> None:
    """Copy the directory/file src to the directory/file target"""
    source_dirname = path.dirname(src)
    for source in iglob(src, recursive=True):
        print("source", source, source_dirname)
        print("thing", source.replace(source_dirname, path.dirname(target)))
        _dest = target
        if (path.exists(target) and not f) or source == target:
            return
        if path.isdir(source) and not r:
            raise ValueError("Source ({}) is directory; use r=True")
        if path.isfile(source) and path.isdir(target):
            _dest = path.join(target, path.basename(source))
        if path.isfile(source) or path.islink(source):
            print(source.replace(source_dirname, _dest))
            # cp_file(source, source.replace(source_dirname, _dest))
            cp_file(source, _dest)
        if path.isdir(source):
            cp_dir(source, _dest)


def ls(dirpath: str = ".", abs: bool = False) -> List[str]:
    """

    :param dirpath:
    :param abs:
    :return:
    """
    if abs:
        return [path.join(dirpath, item) for item in listdir(dirpath)]
    return listdir(dirpath)


def ls_files(dirpath: str = ".", abs: bool = False) -> List[str]:
    """

    :param dirpath:
    :param abs:
    :return:
    """
    files = (file for file in ls(dirpath, abs=True) if path.isfile(file))
    if not abs:
        return list(map(lambda el: el.replace(dirpath, "."), files))
    return list(files)


def ls_dirs(dirpath: str = ".", abs: bool = False) -> List[str]:
    """

    :param dirpath:
    :param abs:
    :return:
    """
    dirs = (dir for dir in ls(dirpath, abs=True) if path.isdir(dir))
    if not abs:
        return list(map(lambda el: el.replace(dirpath, "."), dirs))
    return list(dirs)


def ls_files_dirs(dirpath: str = ".", abs: bool = False) -> Tuple[List[str], List[str]]:
    """

    :param dirpath:
    :param abs:
    :return:
    """
    return ls_files(dirpath, abs=abs), ls_dirs(dirpath, abs=abs)


def rm(path_string: str, r: bool = False, v: bool = False):
    """rm should act like the (ba)sh-rm

    This function was implemented by my cousin Matty-Ice (AKA Matt Bommer)

    :param path_string:
    :param r:
    :param v:
    :return:
    :rtype:

    """
    for _path_str in iglob(path_string, recursive=True):
        try:
            remove(_path_str)
            if v:
                print("Removed file: {}".format(_path_str))

        except Exception as e:
            if r:
                rmtree(_path_str)
                if v:
                    print("Removed dir: {}".format(_path_str))
            else:
                raise ValueError(_path_str + " is a directory -- use r=True")


def basename(path_str: str) -> str:
    """Get the parent-directory for a file or directory path as a string

    :param path_str:
    :return: The parent directory as a string

    .. doctest:: python

        >>> from os import getcwd
        >>> basename(getcwd()) in getcwd()
        True

    """
    return path.split(path.abspath(path_str))[-1]


def dirname(fdpath: str) -> str:
    """Return the parent directory for the given file or dir path

    :param fdpath: file/dir-path as as string
    :return: parent directory for the given file or dir path


    .. doctest:: python

        >>> from os import path
        >>> dirname(path.abspath(__file__)) in path.abspath(__file__)
        True

    """
    return path.split(fdpath)[0]


def export(key: str, val: Union[None, str] = None) -> None:
    """

    :param key:
    :param val:
    :return:
    """
    if val:
        environ[key] = val
        return
    if "=" in key:
        _key, *val = key.split("=")
        export(_key, "=".join(val))


@mkdirs
def touch(filepath: str) -> None:
    """Touches a file just like touch on the command line

    :param filepath: filepath to 'touch' in a unix-y sense
    :return: None
    """
    with open(filepath, "a"):
        utime(filepath, None)


def shebang(filepath: str) -> Union[None, str]:
    """returns the shebang path given a filepath or None if it does not exist.

    :param filepath: path to a file w/ a shebange line
    :return: shebang line or None

    .. doctest::python

        >>> from inspect import getabsfile
        >>> script = 'ashellscript.sh'
        >>> with open(script, 'w') as f:
        ...     f.write('#!/bin/bash\\necho "howdy"\\n')
        25
        >>> shebang(script)
        '#!/bin/bash'
        >>> from os import remove
        >>> remove(script)

    """
    with open(filepath, "r") as f:
        first = f.readline().strip("\n")
        return first if "#!" in first[:2] else None


path2name = basename  # Alias for basename
parent_dirpath = dirname  # Alias for dirname
# Operating system dependent things
link_dir = _OS.link_dir
link_dirs = _OS.link_dirs
link_file = _OS.link_file
link_files = _OS.link_files
unlink_dir = _OS.unlink_dir
unlink_dirs = _OS.unlink_dirs
unlink_file = _OS.unlink_file
unlink_files = _OS.unlink_files
sync = _OS.sync
echo = print
