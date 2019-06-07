# -*- coding: utf-8 -*-
"""
========
IN & OUT
========
"""
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
