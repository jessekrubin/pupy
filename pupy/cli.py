# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
"""
========
Pupy CLI
========
"""
from argparse import ZERO_OR_MORE
from argparse import ArgumentParser
from codecs import decode
from os import listdir
from os import rename

from pupy._version import __version__


def unescaped_str(arg_str):
    """

    :param arg_str:
    :return:
    """
    return decode(str(arg_str), "unicode_escape")


parser = ArgumentParser(description="Command description.")
parser.add_argument(
    "-r", "--replace", metavar="PAT", nargs=2, help="Rename all things in."
)
parser.add_argument("-V", "--version", action="store_true", help="Print pupy version.")
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
