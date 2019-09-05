# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python
from sys import stdout


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
