# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python
"""
=========
Shell-ish
=========
"""
from os import chdir
from os import getcwd
from os import listdir
from os import lstat
from os import makedirs
from os import path
from os import readlink
from os import remove
from os import rename
from os import stat
from os import symlink
from os import unlink
from platform import system
from shutil import copy2
from shutil import copystat
from shutil import rmtree
from subprocess import PIPE
from subprocess import run
from typing import List
from typing import Tuple


class LIN:
    @staticmethod
    def rsync_args(
        src, dest, delete=False, mkdirs=False, exclude=[], include=[], dry_run=False
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

        """
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
    def rsync(src, dest, delete=False, exclude=[], include=[], dry_run=False):
        """Sheldon rsync wrapper for syncing tdirs

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
        symlink(targetpath, linkpath)

    @staticmethod
    def link_dirs(link_target_tuples):
        for link, target in link_target_tuples:
            LIN.link_dir(link, target)

    @staticmethod
    def link_file(linkpath: str, targetpath: str) -> None:
        makedirs(path.split(linkpath)[0], exist_ok=True)
        symlink(targetpath, linkpath)

    @staticmethod
    def link_files(link_target_tuples):
        for link, target in link_target_tuples:
            LIN.link_file(link, target)

    @staticmethod
    def unlink_dir(link):
        unlink(link)

    @staticmethod
    def unlink_dirs(links):
        for link in links:
            unlink(link)

    @staticmethod
    def unlink_file(link):
        unlink(link)

    @staticmethod
    def unlink_files(links):
        for link in links:
            unlink(link)

    sync = rsync


class WIN:

    # def rsync_args(src, dest,
    #                delete=False, mkdirs=False,
    #                exclude=[], include=[], dry_run=False):
    @staticmethod
    def robocopy_args(
        src, dest, delete=False, exclude_files=[], exclude_dirs=[], dry_run=False
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

        """
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
        src, dest, delete=False, exclude_files=[], exclude_dirs=[], dry_run=False
    ):
        """Robocopy for sheldon

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
        makedirs(link, exist_ok=True)
        run(args=["mklink", "/D", link, target], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def link_dirs(link_target_tuples):
        def _check_link_target(link, target):
            # for link, target in link_target_tuples:
            try:
                assert path.exists(target) and path.isdir(target)
                # makedirs(path.split(link)[0], exist_ok=True)
                # _exists.extend(["mklink", link, target, "&&"])
                # _exists.extend(["mklink", link, target, "&&"])
            except AssertionError as e:
                print(
                    "Link target not found; unable to create link:\n    {} => {}".format(
                        link, target
                    )
                )
                return False
            except Exception as e:
                print(e, type(e))
            try:
                rmtree(link)

            except:
                pass
            return True

        _exists = [
            "mklink /D {} {}".format(link, target)
            for link, target in link_target_tuples
            if _check_link_target(link, target)
        ]
        run(args=" && ".join(_exists).split(" "), stdout=PIPE, stderr=PIPE, shell=True)
        # link_args = []
        # for link, target in link_target_tuples:
        #     makedirs(link, exist_ok=True)
        #     link_args.extend(["mklink", "/D", link, target, "&&"])
        # run(args=link_args[:-1], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def link_file(link, target):
        makedirs(path.split(link)[0], exist_ok=True)
        run(args=["mklink", link, target], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def link_files(link_target_tuples):
        def _check_link_target(link, target):
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
            except Exception as e:
                print(e, type(e))
            return False

        _exists = [
            "mklink {} {}".format(link, target)
            for link, target in link_target_tuples
            if _check_link_target(link, target)
        ]
        run(args=" && ".join(_exists).split(" "), stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def unlink_dir(link):
        run(args=["RD", link], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def unlink_dirs(links):
        cmd_args = " && ".join("RD {}".format(link) for link in links).split(" ")
        run(args=cmd_args, stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def unlink_file(link):
        run(args=["Del", link], stdout=PIPE, stderr=PIPE, shell=True)

    @staticmethod
    def unlink_files(links):
        cmd_args = " && ".join("Del {}".format(link) for link in links).split(" ")
        run(args=cmd_args, stdout=PIPE, stderr=PIPE, shell=True)

    sync = robocopy


# _OS = system().lower()
_OS = WIN if "win" in system().lower() else LIN

mv = rename
pwd = getcwd
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
                from os import lchmod

                st = lstat(_src_pth)
                mode = stat.S_IMODE(st.st_mode)
                lchmod(_dest_pth, mode)
            except:
                pass
        elif path.isdir(_src_pth):
            if r:
                cp(_src_pth, _dest_pth, r=True, symlinks=symlinks, ignore=ignore)
            else:
                print("{} is dir; use rm(..., r=True)".format(_src_pth))
        else:
            copy2(_src_pth, _dest_pth)


def ls(dirpath: str = ".", abs: bool = False) -> List[str]:
    if abs:
        return [path.join(dirpath, item) for item in listdir(dirpath)]
    return listdir(dirpath)


def ls_files(dirpath: str = ".", abs: bool = False) -> List[str]:
    files = (file for file in ls(dirpath, abs=True) if path.isfile(file))
    if not abs:
        return list(map(lambda el: el.replace(dirpath, "."), files))
    return list(files)


def ls_dirs(dirpath: str = ".", abs: bool = False) -> List[str]:
    dirs = (dir for dir in ls(dirpath, abs=True) if path.isdir(dir))
    if not abs:
        return list(map(lambda el: el.replace(dirpath, "."), dirs))
    return list(dirs)


def ls_files_dirs(dirpath: str = ".", abs: bool = False) -> Tuple[List[str], List[str]]:
    return ls_files(dirpath, abs=abs), ls_dirs(dirpath, abs=abs)


def rm(*args, r=False):
    for _path_str in args:
        if path.isfile(_path_str):
            remove(_path_str)
        elif path.isdir(_path_str):
            if r:
                rmtree(_path_str)
            else:
                print("{} is dir; use rm(..., r=True)".format(_path_str))


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


# def link_dir(link, target):
#     return _OS.link_dir(link, target)
link_dir = _OS.link_dir
link_dirs = _OS.link_dirs
link_file = _OS.link_file
link_files = _OS.link_files
unlink_dir = _OS.unlink_dir
unlink_dirs = _OS.unlink_dirs
unlink_file = _OS.unlink_file
unlink_files = _OS.unlink_files
sync = _OS.sync
# def link_dirs(link_target_tuples):
#     return _OS.link_dirs(link_target_tuples)
#
# def link_file(link, target):
#     _link = win.link_file if "win" in _OS else lin.link_file
#     makedirs(parent_dirpath(link), exist_ok=True)
#     return _OS.link_file(link, target)
#
# def link_files(link_target_tuples):
#     _link = win.link_files if "win" in _OS else lin.link_files
#     link_target_tuples = list(link_target_tuples)
#     for link, target in link_target_tuples:
#         makedirs(parent_dirpath(link), exist_ok=True)
#     _link(link_target_tuples)
#     for link, target in link_target_tuples:
#         makedirs(parent_dirpath(link), exist_ok=True)

# def unlink_dir(link_path: str):
#     _unlink = win.unlink_dir if "win" in _OS else lin.unlink_dir
#     return _unlink(link_path)
#
# def unlink_dirs(link_paths):
#     try:
#         _unlink = win.unlink_dirs if "win" in _OS else lin.unlink_dirs
#         return _unlink(link_paths)
#     except TypeError:
#         pass
#
# def unlink_file(link):
#     _unlink = win.unlink_file if "win" in _OS else lin.unlink_file
#     return _unlink(link)
#
# def unlink_files(links):
#     try:
#         _unlink = win.unlink_files if "win" in _OS else lin.unlink_files
#         return _unlink(links)
#     except TypeError:
#         pass

# def sync(src, dest):
#     """Update (rsync/robocopy) a local test directory from raid
#
#     :param dest: path to local tdir
#     :param src: path to remote tdir
#     :return: subprocess return code for rsync/robocopy
#     """
#     _sync = win.robocopy if "win" in _OS else lin.rsync
#     return _sync(src=src, dest=dest)
