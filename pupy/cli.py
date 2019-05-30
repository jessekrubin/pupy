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
import sys
from argparse import ArgumentParser
from argparse import FileType
from os import listdir
from os import path

##### PUPY #####
# from pupy import ljson
# from pupy import lstr
# from pupy import sjson
# from pupy import sstr
# from pupy import files_gen
# from pupy import dirs_gen
##### PUPY #####

PARSER = ArgumentParser(description="python scripty.py < stdin > stdout")

_INS = PARSER.add_mutually_exclusive_group()
_INS.add_argument(
    "--input",
    "-i",
    type=FileType("r"),
    default=sys.stdin,
    help="Input file name; or stdin.",
)
_INS.add_argument("jasm", nargs="?", type=str, help="Input string")
PARSER.add_argument(
    "--output",
    "-o",
    type=FileType("w"),
    help="Output file name; or stdout",
    default=sys.stdout,
)


def main():
    ARGV = PARSER.parse_args()
    input_str = ARGV.jasm or ARGV.input.read()
    ARGV.output.write(input_str)
    ARGV.output.write("ooooouuuuuuuttttt")
    ARGV.output.write("\n")


if __name__ == "__main__":
    main()
"""

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

parser.add_argument(
    "-io", "--in-n-out",
    metavar="script name",
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
    if args.in_n_out:
        print(args.in_n_out)
        for fname in args.in_n_out:
            if not fname.endswith('.py'):
                fname = fname + '.py'
            sstring(fname, _IN_N_OUT)

