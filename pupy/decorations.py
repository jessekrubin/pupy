# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from __future__ import division
from __future__ import print_function

from cProfile import Profile
from functools import wraps
from inspect import getfile
from os import chdir
from os import getcwd
from os import makedirs
from os import path, mkdir
from time import time
from typing import Callable
from typing import Tuple


def in_n_out(funk: Callable):
    """Chdir in to the dir the test_function is in and change dirs out when done

    :type funk: Callable
    :param funk: docin.api logger functions logger.(debug/info/warn/error)
    :return: wrapped function
    """

    @wraps(funk)
    def chin_n_chout(*args: Tuple[str, ...], **kwargs: object):
        """

        :param args:
        :param kwargs:
        :return:
        """
        # thing = os.path.split(os.path.realpath(__file__))
        cd = getcwd()
        dirpath = args[0]
        if path.isdir(dirpath):
            chdir(dirpath)
        funk_results = funk(*args, **kwargs)
        chdir(cd)
        return funk_results

    return chin_n_chout


def flog(funk: Callable):
    """Function Log

    :type funk: Callable
    :param funk: docin.api logger functions logger.(debug/info/warn/error)
    :return: wrapped function
    """
    fn = funk.__name__.upper()

    def _fmt_arg(arg):
        return "\n[[%s ~ %s]]" % (fn, arg)  # $# log level string and message

    def _fmt_log_level(args: Tuple[object, ...]) -> str:
        return "\n".join(
            _fmt_arg(arg)  # $# formmat the msg string...
            for arg in args  # $# ...for each msg arg in args...
            if type(arg) == str
        )  # $# ...for string args

    @wraps(funk)
    def log_to_console_wrapper(*args: Tuple[str, ...], **kwargs: object) -> Callable:
        """

        :param args:
        :param kwargs:
        :return:
        """
        # if False:  # NOT DEBUGGING
        #     logging.info(_fmt_log_level(args))
        return funk(*args, **kwargs)

    return log_to_console_wrapper


def mkdirs(funk):
    @wraps(funk)
    def _wrapper(*args, **kwargs):
        dirpath = path.split(args[0])[0]
        try:
            makedirs(dirpath, exist_ok=True)
        except OSError:
            pass
        return funk(*args, **kwargs)

    return _wrapper


def dirdec(funk):
    @wraps(funk)
    def _wrapper(*args, **kwargs):
        result = funk(*args, **kwargs)
        try:
            if not path.exists(result):
                mkdir(result)
        except OSError:
            pass
        return result

    return _wrapper


def cash_it(funk):
    """args-2-return value cache.
    
    This function is particularly useful for when you want that lru-cache,
    but you/one is working with python two.

    :param funk: function to be cached
    :type funk: function
    :returns: wrapped function
    :rtype: function

    """
    cash_money = {}

    @wraps(funk)
    def cash_wrap(*argz):
        """

        """
        if argz not in cash_money:
            rv = funk(*argz)
            cash_money[argz] = rv
        return cash_money[argz]

    return cash_wrap


def cprof(funk):
    """"cProfiling decorator
    
    src: https://zapier.com/engineering/profiling-python-boss/

    :param funk: 

    """

    @wraps(funk)
    def profiled_funk(*args, **kwargs):
        """

        """
        profile = Profile()
        try:
            profile.enable()
            ret_val = funk(*args, **kwargs)
            profile.disable()
        finally:
            print("__CPROFILE__")
            profile.print_stats()
        return ret_val

    return profiled_funk


class tictoc(object):
    """Timing decorator object

    :param runs: # of runs to time over (defaults to 1)

    """

    def __init__(self, runs=1):
        self.runs = runs

    def __str__(self, t_total, funk, args_string):
        str_list = [
            "__TICTOC__",
            "    file: {}".format(getfile(funk)),
            "    funk: {}".format(funk.__name__),
            "    args: {}".format(args_string),
            "    time: {}".format(tictoc.ftime(t_total)),
            "    runs: {}".format(self.runs),
        ]
        return "\n".join(str_list)

    def __call__(self, time_funk, printing=True):
        @wraps(time_funk)
        def time_wrapper(*args, **kwargs):
            """

            """
            self.args = str(args)
            ts = time()
            for i in range(self.runs):
                result = time_funk(*args, **kwargs)
            te = time()
            t_total = (te - ts) / self.runs
            if printing:
                print(self.__str__(t_total, time_funk, str(args)))
            return result

        return time_wrapper

    @staticmethod
    def ftime(t1, t2=None):
        """Formats time string
        
        Formats t1 if t2 is None as a string; Calculates the time and formats
        the time t2-t1 if t2 is not None.

        :param t1: time 1
        :type t1: double
        :param t2: time 2 (Default value = None)
        :type t2: None or double
        :returns: -> formated time string
        :rtype: str

        """
        if t2 is not None:
            return tictoc.ftime((t2 - t1))
        elif t1 == 0.0:
            return "~0.0~"
        elif t1 >= 1:
            return "%.3f s" % t1
        elif 1 > t1 >= 0.001:
            return "%.3f ms" % ((10 ** 3) * t1)
        elif 0.001 > t1 >= 0.000001:
            return "%.3f μs" % ((10 ** 6) * t1)
        elif 0.000001 > t1 >= 0.000000001:
            return "%.3f ns" % ((10 ** 9) * t1)
        else:
            return tictoc.ftime((t2 - t1))
