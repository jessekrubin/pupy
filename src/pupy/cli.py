# -*- coding: utf-8 -*-
"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mpupy` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``pupy.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``pupy.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
from argparse import ArgumentParser
from argparse import ZERO_OR_MORE
from codecs import decode
from os import listdir
from os import rename

from pupy._version import __version__

def unescaped_str(arg_str):
    return decode(str(arg_str), "unicode_escape")

parser = ArgumentParser(description="Command description.")
parser.add_argument(
    "-r", "--replace", metavar="PAT", nargs=2, help="Rename all things in."
)
parser.add_argument(
    "-V", "--version", action="store_true", help="Print pupy version."
)
parser.add_argument(
    "--rm-pattern",
    metavar="PAT",
    type=unescaped_str,
    nargs=ZERO_OR_MORE,
    help="REPLACE pattern with a space.",
)

def main(args=None):
    """

    :param args:
    """

    args = parser.parse_args(args=args)
    if args.version:
        print("Pupy version: {}".format(__version__))
    if args.replace:
        frum, two = args.replace
        print("Replacing:", frum)
        print("With:", two)
        for f in listdir("."):
            print("For f/d:", f)
            rename(f, f.replace(frum, two))

    if args.rm_pattern:
        for pattern in args.rm_pattern:
            print("Removing pattern:", pattern)
            for f in listdir("."):
                print("For f/d:", f)
                rename(f, f.replace(pattern, ""))
# http://192.168.1.225:5984/
