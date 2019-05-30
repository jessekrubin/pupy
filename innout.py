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
