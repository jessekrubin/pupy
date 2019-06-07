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
from pupy.savings_n_loads import sstring
from pupy._version import __version__

_IN_N_OUT = """# -*- coding: utf-8 -*-
\"\"\"
========
IN & OUT
========
\"\"\"
__version__ = "0.0.0"
import sys
from argparse import ArgumentParser
from argparse import FileType
from os import listdir
from os import path

# from pupy import ljson      #$# load json from filepath (filepath)
# from pupy import lstr       #$# load str from filepath (filepath)
# from pupy import sjson      #$# save json to filepath (filepath, data)
# from pupy import sstr       #$# save str to filepath (filepath, string)
# from pupy import files_gen  #$# gen filepaths below directory (dirpath)
# from pupy import dirs_gen   #$# gen dirpaths below directory (dirpath)

PARSER = ArgumentParser(description="python scripty.py < stdin > stdout")

_INS = PARSER.add_mutually_exclusive_group()
_INS.add_argument(
    "-i",
    "--input",
    type=FileType("r"),
    default=sys.stdin,
    metavar="IN",
    help="Input file name; or stdin.",
)
_INS.add_argument(
    "strinput", nargs="?", type=str, metavar="STDIN", help="Input string via"
)
PARSER.add_argument(
    "-o",
    "--output",
    type=FileType("w"),
    help="Output file name (defaults to STDOUT)",
    default=sys.stdout,
)


def main():
    ARGV = PARSER.parse_args()
    input_str = ARGV.strinput or ARGV.input.read()
    ARGV.output.write(input_str)
    ARGV.output.write("OUTPUT\n")


if __name__ == "__main__":
    main()
"""


def unescaped_str(arg_str):
    """

    :param arg_str:
    :return:
    """
    return decode(str(arg_str), "unicode_escape")


PARSER = ArgumentParser(description="Command description.")
PARSER.add_argument(
    "-r", "--replace", metavar="PAT", nargs=2, help="Rename all things in."
)
PARSER.add_argument("-V", "--version", action="store_true", help="Print pupy version.")
PARSER.add_argument(
    "--rm-pattern",
    metavar="PAT",
    type=unescaped_str,
    nargs=ZERO_OR_MORE,
    help="REPLACE pattern with a space.",
)

PARSER.add_argument(
    "-io",
    "--in-n-out",
    metavar="script name",
    type=unescaped_str,
    nargs=ZERO_OR_MORE,
    help="REPLACE pattern with a space.",
)


def main(ARGS=None):
    """

    :param ARGS:
    """

    ARGS = PARSER.parse_args(args=ARGS)
    if ARGS.version:
        print("Pupy version: {}".format(__version__))
    if ARGS.replace:
        frum, two = ARGS.replace
        print("Replacing:", frum)
        print("With:", two)
        for f in listdir("."):
            print("For f/d:", f)
            rename(f, f.replace(frum, two))

    if ARGS.rm_pattern:
        for pattern in ARGS.rm_pattern:
            print("Removing pattern:", pattern)
            for f in listdir("."):
                print("For f/d:", f)
                rename(f, f.replace(pattern, ""))
    if ARGS.in_n_out:
        print(ARGS.in_n_out)
        for fname in ARGS.in_n_out:
            if not fname.endswith(".py"):
                fname = fname + ".py"
            sstring(fname, _IN_N_OUT.strip("\n").strip("\r\n") + "\n")
