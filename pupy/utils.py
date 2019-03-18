# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from os import path, stat
from datetime import datetime

def fmt_bytes(num):
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

def fmt_file_size(filepath):
    """
    this function will return the file size
    """
    if path.isfile(filepath):
        file_info = stat(filepath)
        return fmt_bytes(file_info.st_size)

def fmt_seconds(t1, t2=None):
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

def path2name(path_str):
    """Get the parent-directory for a file or directory path as a string

    :param somepath: path as a string which ya would like the parent of
    :return: The parent directory as a string

    .. doctest:: python

        >>> from os import getcwd
        >>> path2name(getcwd()) in getcwd()
        True

    """
    return path.split(path.abspath(path_str))[-1]

def parent_dirpath(fdpath):
    """

    :param fdpath: file/dir-path as as string
    :return:

    .. doctest:: python

        >>> from os import path
        >>> parent_dirpath(path.abspath(__file__)) in path.abspath(__file__)
        True

    """
    return path.split(fdpath)[0]

def timestamp(ts=None):
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
