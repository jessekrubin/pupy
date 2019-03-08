# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
"""
String Methods
"""


def binary_string(number):
    """Number to binary string

    :param number: some number (an integer) to turn into a binary string
    :return: Some string which is the binary string

    .. doctest:: python

        >>> binary_string(200)
        '11001000'
        >>> binary_string(10)
        '1010'

    """
    return bin(number)[2:]


def string_score(strang):
    """Sum of letter values where a==1 and z == 26

    :param strang: string to be scored
    :type strang: str
    :returns: -> score of the string
    :rtype: int

    .. doctest:: python

        >>> string_score('me')
        18
        >>> string_score('poooood')
        95
        >>> string_score('gregory')
        95

    """
    return sum((ord(character) - 96 for character in strang.lower()))


def is_palindrome(string):
    """True a string is a palindrome; False if string is not a palindrome.

    :param string: 

    .. doctest::python

        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("greg")
        False

    """
    return all(
        character == string[-index - 1] for index, character in enumerate(string)
    )
