# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python
"""
========
Pupy CLI
========
"""
from argparse import ZERO_OR_MORE
from argparse import ArgumentParser
from codecs import decode
from os import makedirs
from os import path as _path

from pupy._template import _IO_PKG_CLI
from pupy._template import _IO_SCRIPT
from pupy._template import _PKG_INIT
from pupy._template import _PKG_MAIN
from pupy._template import _PKG_UTILS
from pupy._version import __version__
from pupy.savings_n_loads import sstring
from pupy.sh import pwd


def unescaped_str(arg_str):
    """

    :param arg_str:
    :return:
    """
    return decode(str(arg_str), "unicode_escape")


def new_package(relative_path):
    try:
        makedirs(relative_path, exist_ok=False)
        relative_path
        sstring(
            _path.join(relative_path, "__init__.py"),
            _PKG_INIT.strip("\n").strip("\r\n") + "\n",
        )
        sstring(
            _path.join(relative_path, "__main__.py"),
            _PKG_MAIN.strip("\n").strip("\r\n") + "\n",
        )
        sstring(
            _path.join(relative_path, "cli.py"),
            _IO_PKG_CLI.strip("\n").strip("\r\n") + "\n",
        )
        sstring(
            _path.join(relative_path, "utils.py"),
            _PKG_UTILS.strip("\n").strip("\r\n") + "\n",
        )
        print("Created package: {}".format(relative_path))
    except:
        raise ValueError("{} already exists".format(relative_path))
        return


def new_cmd(args):
    if args.package:
        for relpath in args.path:
            new_package(relpath)
        return

    for fname in args.path:
        if not fname.endswith(".py"):
            fname = fname + ".py"
        new_filepath = _path.join(pwd(), fname)
        sstring(new_filepath, _IO_SCRIPT.strip("\n").strip("\r\n") + "\n")
        print("Created script: {}".format(new_filepath))


PARSER = ArgumentParser(description="Command description.")
SUBPARSERS = PARSER.add_subparsers(help="commands")
PARSER.add_argument("-V", "--version", action="store_true", help="Print pupy version.")

NEW_SUBPARSER = SUBPARSERS.add_parser("new")
NEW_SUBPARSER.add_argument(
    "path", type=unescaped_str, nargs=ZERO_OR_MORE, help="relative path"
)
NEW_SUBPARSER.add_argument(
    "-p", "--package", action="store_true", default=False, help="new package"
)
NEW_SUBPARSER.set_defaults(func=new_cmd)


def main(ARGS=None):
    """

    :param ARGS:
    """

    ARGS = PARSER.parse_args(args=ARGS)
    if ARGS.version:
        print("pupy version: {}".format(__version__))
    if ARGS.func:
        ARGS.func(ARGS)
