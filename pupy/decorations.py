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
from pupy.utils import fmt_seconds
import logging
from logging.config import dictConfig

# "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
logging_config = dict(
    version=1,
    formatters={
        'f': {
            'format': "[%(levelname)1.1s %(asctime)s %(filename)s:%(lineno)d] %(message)s"
            }
        },
    handlers={
        'h': {
            'class'    : 'logging.StreamHandler',
            'formatter': 'f',
            'level'    : logging.DEBUG
            }
        },
    root={
        'handlers': ['h'],
        'level'   : logging.DEBUG,
        },
    )

dictConfig(logging_config)

logger = logging.getLogger()

def in_n_out(funk: Callable):
    """Chdir in to the dir the test_function is in and change dirs out when done

    :type funk: Callable
    :param funk: docin.api logger functions logger.(debug/info/warn/error)
    :return: wrapped function
    """

    @wraps(funk)
    def chin_n_chout(*args, **kwargs):
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

def flog(funk=None, loglevel='debug', funk_call=True, tictoc=False):
    D = {
        'debug': logger.debug,
        'info' : logger.info,
        'warn' : logger.warning,
        'error': logger.error
        }

    def _decorate_flog_wrapper(_funk):
        def _fmt_args(*args):
            return ", ".join(str(arg) for arg in args)

        def _fmt_kwargs(**kwargs):
            return ", ".join("{}={}".format(str(k), str(v))
                             for k, v in kwargs.items())

        def _fmt_call(*args, **kwargs):
            params_str = ", ".join(
                s for s in (_fmt_args(*args), _fmt_kwargs(**kwargs)) if s
                )
            return "{}({})".format(_funk.__name__, params_str)

        @wraps(_funk)
        def _flog_wrapper(*args, **kwargs):
            ti = time()
            _ret = _funk(*args, **kwargs)
            tf = time()
            msg_parts = [_fmt_call(*args, **kwargs) if funk_call else None,
                         fmt_seconds(ti, tf) if tictoc else None]
            msg_str = ' | '.join(part for part in msg_parts if part)
            if any(el for el in msg_parts):
                D[loglevel]("[FLOG] | {}".format(msg_str))
            return _ret

        return _flog_wrapper

    return _decorate_flog_wrapper(funk) if funk else _decorate_flog_wrapper

def dirdec(funk):
    @wraps(funk)
    def _wrapper(*args, **kwargs):
        result = funk(*args, **kwargs)
        try:
            mkdir(result)
        except (FileExistsError, OSError) as e:
            pass
        return result

    return _wrapper

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
