# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
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
