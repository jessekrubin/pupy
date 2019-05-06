# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from collections import Counter
from collections import deque
from functools import reduce
from operator import mul
from os import path
from os import sep
from os import walk
from typing import Any
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Tuple
from typing import Union

from pupy._typing import Flint


def files_gen(dirpath: str = ",", abs: bool = True) -> Iterator[Any]:
    """Yields paths beneath dirpath param; dirpath defaults to os.getcwd()

    :param dirpath: Directory path to walking down/through.
    :param abs: Yield the absolute path
    :return: Generator object that yields filepaths (absolute or relative)

    """
    return (
        fpath if abs else fpath.replace(dirpath, "").strip(sep)
        for fpath in (
            path.join(pwd, file) for pwd, dirs, files in walk(dirpath) for file in files
        )
    )


def dirs_gen(dirpath: str = ".", abs: bool = True) -> Iterator[Any]:
    """Yields paths beneath dirpath param; dirpath defaults to os.getcwd()

    :param dirpath: Directory path to walking down/through.
    :param abs: Yield the absolute path
    :return: Generator object that yields dir-paths (absolute or relative)

    """
    return (
        fpath if abs else fpath.replace(dirpath, "").strip(sep)
        for fpath in (pwd for pwd, dirs, files in walk(dirpath))
    )


def exhaust(it: Iterable[Any]) -> None:
    """Exhaust an interable / use it up; useful for evaluating a map object.

    :param it: iterable object to run through
    :return: None

    .. docstring::python

        >>> a = [1, 2, 3, 4, 5, 6]
        >>> a_map = map(lambda x: x*2, a)
        >>> a_exhausted = exhaust(a_map)
        >>> a_exhausted == None # will be none after being exhausted
        True

    """
    deque(it, maxlen=0)


def chunks(it: Union[List[int], str], chunk_size: int) -> Iterator[Any]:
    """Yields chunks of something slicable with length <= chunk_size

    :param it:
    :param chunk_size: size of the chunks
    :type chunk_size: int

    .. docstring::python

        >>> list(chunks([1, 2, 3, 4, 5, 6], 3))
        [[1, 2, 3], [4, 5, 6]]
        >>> list(chunks([1, 2, 3, 4, 5, 6], 2))
        [[1, 2], [3, 4], [5, 6]]
        >>> list(chunks('abcdefghijklmnopqrstuvwxyz', 2))
        ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'mn', 'op', 'qr', 'st', 'uv', 'wx', 'yz']
        >>> list(chunks('abcdefghijklmnopqrstuvwxyz', 13))
        ['abcdefghijklm', 'nopqrstuvwxyz']

    """
    return (it[i : i + chunk_size] for i in range(0, len(it), chunk_size))


def is_permutation(
    a: Union[int, List[int], str], b: Union[int, List[int], str]
) -> bool:
    """Checks if two integers or lists are permutations lists are permutations

    :param a: possible perumtation of b
    :type a: int or list
    :param b: possible perumtation of a
    :type b: int or list
    :returns: True if a and b are permutations of one another; False otherwise
    :rtype: bool

    It works for list!!!

    .. doctest:: python

        >>> a = [1, 2, 3, 4]
        >>> b = [4, 3, 2, 1]
        >>> is_permutation(a, b)
        True
        >>> a = [1, 3, 2, 4]
        >>> b = [4, 3, 2, 1]
        >>> is_permutation(a, b)
        True
        >>> a = [1, 3, 2, 4]
        >>> b = [4, 3, 2, 1, 1]
        >>> is_permutation(a, b) # False cuz of the extra 'one'
        False

    It works for integers!?!?!?

    .. doctest:: python

        >>> a = 1234
        >>> b = 4321
        >>> is_permutation(a, b)
        True
        >>> a = 12344
        >>> b = 43212
        >>> is_permutation(a, b)
        False

    It also works for strings!!!

    .. doctest:: python

        >>> a = 'abcd'
        >>> b = 'dbca'
        >>> is_permutation(a, b) # False cuz of the extra 'one'
        True
        >>> a = 'pood'
        >>> b = 'doop'
        >>> is_permutation(a, b) # False cuz of the extra 'one'
        True
        >>> a = 'snorkel'
        >>> b = 'doop'
        >>> is_permutation(a, b) # False cuz of the extra 'one'
        False

    """

    if isinstance(a, int):
        a = digits_list(a)
    if isinstance(b, int):
        b = digits_list(b)
    return len(a) == len(b) and Counter(a) == Counter(b)


def rotate(rlist: List[int], rn: int = 1, left_rotate: bool = True) -> List[int]:
    """Rotate a list (rlist) by rn indices to the left or right

    :param rlist: list/toople or slicable to be rotated
    :type rlist: list or tuple
    :param rn: steps bywhich to rotate (Default value = 1)
    :type rn: int
    :param left_rotate: True (default) left rotates; False right rotates.
    :type left_rotate: bool
    :returns: rotated list
    :rtype: list

    .. doctest:: python

        >>> rotate([1, 2, 3, 4], left_rotate=True)
        [2, 3, 4, 1]
        >>> rotate([1, 2, 3, 4], left_rotate=False)
        [4, 1, 2, 3]
        >>> rotate([1, 2, 3, 4], rn=4, left_rotate=False)
        [1, 2, 3, 4]

    """

    def _left_rotate(l, n=1):
        """

        :param l: 
        :param n:  (Default value = 1)

        """
        return l[n:] + l[:n]

    def _right_rotate(l, n=1):
        """

        :param l: 
        :param n:  (Default value = 1)

        """
        return l[-n:] + l[:-n]

    return _left_rotate(rlist, rn) if left_rotate else _right_rotate(rlist, rn)


def rotations_gen(rlist: Tuple[int, int, int, int]) -> Iterator[Any]:
    """Yields all rotations of a list

    :param rlist:

    .. doctest::python

        >>> for rot in rotations_gen((1, 2, 3, 4)):
        ...     print(rot)
        ...
        (1, 2, 3, 4)
        (4, 1, 2, 3)
        (3, 4, 1, 2)
        (2, 3, 4, 1)

    """
    return ((rlist[-i:] + rlist[:-i]) for i in range(len(rlist)))


def digits_list(number: int) -> List[int]:
    """Returns a list of the digits in num

    :param number: number w/ digits to be listsed
    :type number: int
    :returns: -> digits in a list
    :rtype: list

    .. doctest::python

        >>> digits_list(1111)
        [1, 1, 1, 1]
        >>> digits_list(982)
        [9, 8, 2]
        >>> digits_list(101)
        [1, 0, 1]
        >>> digits_list(123)
        [1, 2, 3]

    """

    digits = deque()
    for _ in range(len(str(number))):
        number, r = divmod(number, 10)
        digits.appendleft(r)
    return list(digits)


def int_from_digits(digits: Iterable[int]) -> int:
    """Converts an iterable of digits digits to a number
    
    The iteratble can be ints or strings/chars

    :rtype: int

    .. doctest::python

        >>> int_from_digits([3, 2, 1])
        321
        >>> int_from_digits([1, 1, 1, 1, 2, 3])
        111123
        >>> int_from_digits([1, 2, 3])
        123

    """
    return sum(
        digits[len(list(digits)) - i - 1] * 10 ** i
        for i in range(0, len(list(digits)), 1)
    )


def iter_product(l: Iterable[int]) -> Flint:
    """Product of all the elements in a list or tuple

    :param l: list with integer elements
    :returns: product of all the elements in a list
    :rtype: int

    .. doctest::python

        >>> iter_product([1, 2, 3, 4])
        24
        >>> iter_product(tuple([1, 2, 3, 4]))
        24
        >>> iter_product([-1, -2, -3, 4])
        -24

    """
    return reduce(mul, l)
