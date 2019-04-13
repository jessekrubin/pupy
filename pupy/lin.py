# -*- coding: utf-8 -*-
from sys import stdout

from subprocess import PIPE
from subprocess import run

def rsync(src, dest):
    """Sheldon rsync wrapper for syncing tdirs

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
    subproc = run(
        args=["rsync", "-a", "-O", "--no-o", "--no-g", "--no-p", "--delete", src, dest],
        stdout=PIPE,
        stderr=PIPE,
        )
    if subproc.returncode != 0:
        stdout.write("\r\n{}\n".format(subproc.stdout))
    return subproc.returncode

def link_dir(link, target):
    pass

def link_dirs(link_target_tuples):
    pass

def link_file(link, target):
    pass

def link_files(link_target_tuples):
    pass

def unlink_dir(link):
    pass

def unlink_dirs(links):
    pass

def unlink_file(link):
    pass

def unlink_files(links):
    pass
