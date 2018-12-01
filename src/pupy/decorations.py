#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from __future__ import division
from __future__ import print_function

import json as jasm
from cProfile import Profile
from functools import wraps
from inspect import getfile
from time import time


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
        if argz in cash_money:
            return cash_money[argz]
        else:
            rv = funk(*argz)
            cash_money[argz] = rv
            return rv
    return cash_wrap

class Jasm(object):
    """Jasm the Grundle Bug"""

    def __init__(self, path):
        self.file_path = path
    def __call__(self, funk):
        """Json saving and loading"""
        fp = self.file_path
        def savings_n_loads(*args, **kwargs):
            """Jasm funk (w)rapper

            """
            if len(args) == 0:
                save_key = "None"
            else:
                save_key = str((args, kwargs.items()))
            try:
                with open(fp) as f:
                    dat_data = jasm.load(f)
            except IOError:
                dat_data = {}
            except ValueError:
                dat_data = {}

            if save_key not in dat_data:
                ret_val = funk(*args, **kwargs)
                dat_data[save_key] = ret_val
                with open(fp, "wb") as f:
                    jasm.dump(dat_data, f, encoding="utf8", sort_keys=True)
            return dat_data[save_key]
        return savings_n_loads
    @staticmethod
    def read(fpath):
        """Jasm load static method

        :param fpath: filepath
        :type fpath: str
        :returns: object/data stored in the json file
        :rtype: object

        """
        with open(fpath) as f:
            return jasm.load(f)
    @staticmethod
    def write(fpath, obj):
        """Jasm dump static method

        :param fpath: filepath
        :type fpath: str
        :param obj: data/object to be saved
        :type obj: object

        """

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
