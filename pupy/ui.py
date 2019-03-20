# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from math import ceil
from shutil import get_terminal_size
from sys import stdout

def yesno(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {
        "yes": True,
        "y"  : True,
        "ye" : True,
        "no" : False,
        "n"  : False
        }
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        out_string = question + prompt
        n_dashes = (
            len(question)
            if "\n" not in question
            else len(question.split("\n")[0])
        )
        out_string = "{}\n{}".format("_" * n_dashes, out_string)
        stdout.write(out_string)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            stdout.write(
                "Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n"
                )

def term_table(strings, row_wise=False, filler='~'):
    max_tname_len = max(len(tname) for tname in strings) + 5
    terminal_cols = get_terminal_size((80, 20)).columns
    table_cols = terminal_cols // max_tname_len
    spaces = " " * ((terminal_cols - (max_tname_len * table_cols)) // table_cols)
    size_string = "{:<" + str(max_tname_len) + "}" + spaces
    fmtstring = size_string * (table_cols - 1)
    fmtstring = fmtstring + "{:<}"
    n_rows = int(ceil(len(strings) / table_cols))
    n_filler_chars = (n_rows * table_cols) - len(strings)
    strings.extend(filler for _ in range(n_filler_chars))
    if row_wise:
        zipper = zip(*(strings[i::table_cols] for i in range(table_cols)))
    else:
        zipper = (strings[i::n_rows] for i in range(n_rows))
    return (fmtstring.format(*row) for row in zipper)
