# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from os import path

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

def parent_path(fdpath):
    """

    :param fdpath:
    :return:

    .. doctest:: python

        >>> from os import path
        >>> parent_path(path.abspath(__file__)) in path.abspath(__file__)
        True

    """
    return path.split(fdpath)[0]
