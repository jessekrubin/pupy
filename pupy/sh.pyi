# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from os import chdir, getcwd, rename
from typing import Any, List, Optional, Tuple

class LIN:
    @staticmethod
    def rsync_args(
        src: Any,
        dest: Any,
        delete: bool = ...,
        mkdirs: bool = ...,
        exclude: Any = ...,
        include: Any = ...,
        dry_run: bool = ...,
    ) -> List[str]: ...
    @staticmethod
    def rsync(
        src: Any,
        dest: Any,
        delete: bool = ...,
        exclude: Any = ...,
        include: Any = ...,
        dry_run: bool = ...,
    ): ...
    @staticmethod
    def link_dir(linkpath: Any, targetpath: Any) -> None: ...
    @staticmethod
    def link_dirs(link_target_tuples: Any) -> None: ...
    @staticmethod
    def link_file(linkpath: str, targetpath: str) -> None: ...
    @staticmethod
    def link_files(link_target_tuples: Any) -> None: ...
    @staticmethod
    def unlink_dir(link: Any) -> None: ...
    @staticmethod
    def unlink_dirs(links: Any) -> None: ...
    @staticmethod
    def unlink_file(link: Any) -> None: ...
    @staticmethod
    def unlink_files(links: Any) -> None: ...
    sync: Any = ...

class WIN:
    @staticmethod
    def robocopy_args(
        src: Any,
        dest: Any,
        delete: bool = ...,
        exclude_files: Any = ...,
        exclude_dirs: Any = ...,
        dry_run: bool = ...,
    ) -> List[str]: ...
    @staticmethod
    def robocopy(
        src: Any,
        dest: Any,
        delete: bool = ...,
        exclude_files: Any = ...,
        exclude_dirs: Any = ...,
        dry_run: bool = ...,
    ): ...
    @staticmethod
    def link_dir(link: Any, target: Any) -> None: ...
    @staticmethod
    def link_dirs(link_target_tuples: Any) -> None: ...
    @staticmethod
    def link_file(link: Any, target: Any) -> None: ...
    @staticmethod
    def link_files(link_target_tuples: Any): ...
    @staticmethod
    def unlink_dir(link: Any) -> None: ...
    @staticmethod
    def unlink_dirs(links: Any) -> None: ...
    @staticmethod
    def unlink_file(link: Any) -> None: ...
    @staticmethod
    def unlink_files(links: Any) -> None: ...
    sync: Any = ...

mv = rename
pwd = getcwd
cd = chdir

def cp(
    src: Any, dst: Any, r: bool = ..., symlinks: bool = ..., ignore: Optional[Any] = ...
) -> None: ...
def ls(dirpath: str = ..., abs: bool = ...) -> List[str]: ...
def ls_files(dirpath: str = ..., abs: bool = ...) -> List[str]: ...
def ls_dirs(dirpath: str = ..., abs: bool = ...) -> List[str]: ...
def ls_files_dirs(
    dirpath: str = ..., abs: bool = ...
) -> Tuple[List[str], List[str]]: ...
def rm(*args: Any, r: bool = ...) -> None: ...
def path2name(path_str: str) -> str: ...
def parent_dirpath(fdpath: str) -> str: ...

link_dir: Any
link_dirs: Any
link_file: Any
link_files: Any
unlink_dir: Any
unlink_dirs: Any
unlink_file: Any
unlink_files: Any
sync: Any
