# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python
"""
String Methods
"""

def string_score(strang: str) -> int:
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

def is_palindrome(string: str) -> bool:
    """True a string is a palindrome; False if string is not a palindrome.

    :param string: 

    .. doctest::python

        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("greg")
        False

    """
    return all(
        character == string[-index - 1]
        for index, character in enumerate(string)
    )

if __name__ == "__main__":
    from doctest import testmod

    testmod()
