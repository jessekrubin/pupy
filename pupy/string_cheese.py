# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
"""
String Methods
"""
from binascii import hexlify
from os import urandom
from re import compile
from re import sub
from string import printable


def bytes2str(bites: bytes, encoding: str = "utf-8") -> str:
    """Convert bytes to a string

    :param bites: bytes
    :type bites: bytes
    :param encoding: encoding of the string (default is utf-8)
    :type encoding: str
    :return: converted bytes
    :rtype: str


    .. doctest:: python

        >>> a = b'abcdefg'
        >>> type(a)
        <class 'bytes'>
        >>> bytes2str(a)
        'abcdefg'
        >>> type(bytes2str(a))
        <class 'str'>

    """
    return bites.decode(encoding)


def binary_string(number: int) -> str:
    """Number to binary string

    :param number: some number (an integer) to turn into a binary string
    :return: Some string which is the binary string
    :rtype: str

    .. doctest:: python

        >>> binary_string(200)
        '11001000'
        >>> binary_string(10)
        '1010'

    """
    return bin(number)[2:]


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
        character == string[-index - 1] for index, character in enumerate(string)
    )


def strip_comments(string):
    filelines = string.splitlines(keepends=False)
    r = compile(r'(?:"(?:[^"\\]|\\.)*"|[^"#])*(#|$)')
    return "\n".join((line[: r.match(line).start(1)] for line in filelines))


def strip_ascii(s: str) -> str:
    """Remove all ascii characters from a string

    :param s: string with non-ascii characters
    :type s: string
    :return: string of only the non-ascii characters

    .. doctest::

        >>> string_w_non_ascii_chars = 'Three fourths: ¾'
        >>> strip_ascii(string_w_non_ascii_chars)
        '¾'

    """
    return "".join(sc for sc in (str(c) for c in s) if sc not in printable)


def no_b(string: str) -> str:
    """Removes the b'' from binary strings and sub-strings that contain b''

    :param string: A string surrounded by b'' or a sub-string with b''
    :return: A string without binary b'' quotes surround it

    .. doctest::

        >>> no_b("b'a_string'")
        'a_string'

    """
    return sub("b'([^']*)'", r"\1", string)


def no_u(string: str) -> str:
    """Removes the u'' from unicode strings and sub-strings that contain u''

    :param string: A string surrounded by u'' or a sub-string with u''
    :return: A string without unicode u'' quotes surround it

    .. doctest:: python

        >>> a = "u'a_string'"
        >>> no_u(a)
        'a_string'


    """
    return sub("u'([^']*)'", r"\1", string)


def rhex_str(length: int = 4) -> str:
    """Returns a random hex string

    :param length: length of random bytes to turn into hex (defaults to 4)
    :type length: int
    :return: random hexadecimal string
    :rtype: str

    .. doctest:: python

        >>> a = rhex_str()
        >>> isinstance(a, str)
        True
        >>> len(a) == 8
        True

    """
    return bytes2str(hexlify(urandom(length)))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
