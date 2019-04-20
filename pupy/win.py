# -*- coding: utf-8 -*-

from subprocess import PIPE
from subprocess import run


def robocopy(src, dest):
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
    subproc = run(["robocopy", src, dest, "/mir", "/mt"], stdout=PIPE, stderr=PIPE)
    if subproc.returncode not in (0, 1, 2, 3):
        print(subproc)
    return subproc.returncode


def link_dir(link, target):
    run(args=["mklink", "/D", link, target], stdout=PIPE, stderr=PIPE, shell=True)


def link_dirs(link_target_tuples):
    link_args = []
    for link_target_tuple in link_target_tuples:
        link_args.extend(["mklink", "/D", *link_target_tuple, "&&"])
    run(args=link_args[:-1], stdout=PIPE, stderr=PIPE, shell=True)


def link_file(link, target):
    run(args=["mklink", link, target], stdout=PIPE, stderr=PIPE, shell=True)


def link_files(link_target_tuples):
    link_args = []
    for link_target_tuple in link_target_tuples:
        link_args.extend(["mklink", *link_target_tuple, "&&"])
    run(args=link_args[:-1], stdout=PIPE, stderr=PIPE, shell=True)


def unlink_dir(link):
    run(args=["RD", link], stdout=PIPE, stderr=PIPE, shell=True)


def unlink_dirs(links):
    cmd_args = " && ".join("RD {}".format(link) for link in links).split(" ")
    run(args=cmd_args, stdout=PIPE, stderr=PIPE, shell=True)


def unlink_file(link):
    run(args=["Del", link], stdout=PIPE, stderr=PIPE, shell=True)


def unlink_files(links):
    cmd_args = " && ".join("Del {}".format(link) for link in links).split(" ")
    run(args=cmd_args, stdout=PIPE, stderr=PIPE, shell=True)
