# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from math import ceil
from shutil import get_terminal_size
from sys import stdout
from typing import Any
from typing import Iterator
from typing import List


def yesno(question, default=True, tries=3):
    """Ask a yes/no question and return an answer as a boolean

    :param question: question to ask a user
    :param default: True=yes; False=no; None=no-default
    :param tries: number of tries before giving up
    :return: True/False depending on the response

    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    default_prompts = {None: "[y/n]", True: "[Y/n]", False: "[y/N]"}
    if default is not None:
        valid[""] = True if default else False
    stdout.write("{} {} ".format(question, default_prompts[default]))
    try:
        return valid[input().lower()]
    except KeyError:
        stdout.write("Valid responses: [y]es/[n]o (case insensitive)\n")
    return yesno(question, default)


def term_table(
    strings: List[str], row_wise: bool = False, filler: str = "~"
) -> Iterator[Any]:
    """

    :param strings:
    :param row_wise:
    :param filler:
    :return:
    """
    max_str_len = max(len(str) for str in strings) + 5
    terminal_cols = get_terminal_size((80, 20)).columns
    n_cols = terminal_cols // max_str_len
    n_rows = int(ceil(len(strings) / n_cols))
    spaces = " " * ((terminal_cols - (max_str_len * n_cols)) // n_cols)
    size_string = "{:<" + str(max_str_len) + "}" + spaces
    fmtstring = size_string * (n_cols - 1) + "{:<}"
    strings.extend(filler for _ in range(n_rows * n_cols - len(strings)))
    if row_wise:
        line_iter = zip(*(strings[i::n_cols] for i in range(n_cols)))
    else:
        line_iter = (strings[i::n_rows] for i in range(n_rows))
    return (fmtstring.format(*row) for row in line_iter)
