# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

_PKG_MAIN: str = """# -*- coding: utf-8 -*-
\"\"\"
=====================
Pretty Useful Package
=====================
\"\"\"

from .cli import main

if __name__ == "__main__":
    main()
    
"""
_PKG_INIT = """# -*- coding: utf-8 -*-
\"\"\"
=====================
Pretty Useful Package
=====================
\"\"\"
"""
_PKG_UTILS = """# -*- coding: utf-8 -*-
\"\"\"
===================
Pretty Useful Utils
===================
\"\"\"
# import sys
# from os import listdir
# from os import path

# from pupy import ljson      #$# load json from filepath (filepath)
# from pupy import lstr       #$# load str from filepath (filepath)
# from pupy import sjson      #$# save json to filepath (filepath, data)
# from pupy import sstr       #$# save str to filepath (filepath, string)
# from pupy import files_gen  #$# gen filepaths below directory (dirpath)
# from pupy import dirs_gen   #$# gen dirpaths below directory (dirpath)
# from pupy import sh         #$# shell-y funks; sh.cd, sh.ls, sh.pwd...

def main():
    pass

if __name__ == "__main__":
    main()
    # from doctest import testmod
    # testmod() 
"""
_IO_SCRIPT = """# -*- coding: utf-8 -*-
\"\"\"
====================
Pretty Useful Script
====================
\"\"\"
__version__ = "0.0.1"
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
# from pupy import sh         #$# shell-y funks; sh.cd, sh.ls, sh.pwd...

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
    # from doctest import testmod
    # testmod() 
"""
_IO_PKG_CLI = _IO_SCRIPT.replace(
    "====================\n" "Pretty Useful Script\n" "====================\n",
    "=====================\n" "Pretty Useful Package\n" "=====================\n",
)

if __name__ == "__main__":
    pass
