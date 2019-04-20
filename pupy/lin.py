# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from os import symlink
from os import unlink
from subprocess import PIPE
from subprocess import run


def rsync(src: str, dest: str, delete: bool = False):
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
     - 30 == Timeout in data send/receive
     - 35 == Timeout waiting for daemon connection

    """
    subproc = run(["mkdir", "-p", dest], stdout=PIPE, stderr=PIPE)
    if not dest.endswith("/"):
        dest = "{}/".format(dest)
    if not src.endswith("/"):
        src = "{}/".format(src)
    rsync_args = [
        "rsync",
        "-a",
        "-O",
        "--no-o",
        "--no-g",
        "--no-p",
        "--delete" if delete else None,
        src,
        dest,
    ]
    subproc = run(args=list(filter(None, rsync_args)), stdout=PIPE, stderr=PIPE)
    return subproc


def link_dir(linkpath, targetpath):
    symlink(targetpath, linkpath)


def link_dirs(link_target_tuples):
    for link, target in link_target_tuples:
        link_dir(link, target)


def link_file(linkpath: str, targetpath: str) -> None:
    symlink(targetpath, linkpath)


def link_files(link_target_tuples):
    for link, target in link_target_tuples:
        link_file(link, target)


def unlink_dir(link):
    unlink(link)


def unlink_dirs(links):
    for link in links:
        unlink(link)


def unlink_file(link):
    unlink(link)


def unlink_files(links):
    for link in links:
        unlink(link)
