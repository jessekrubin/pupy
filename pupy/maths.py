# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from collections import Counter
from math import acos
from math import factorial
from math import pi
from math import sqrt
from operator import add
from operator import floordiv
from operator import methodcaller
from operator import sub
from operator import truediv
from typing import Any
from typing import Iterator
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import Union

from pupy.decorations import cash_it
from pupy.foreign import iter_product


def partitions_gen(numero: int, min_p: int = 1, max_p: Optional[int] = None):
    """Partitions generator

    Adapted from: code.activestate.com/recipes/218332-generator-for-integer-partitions/min_p

    :param numero: number for which to yield partiton tuples
    :type numero: int
    :param min_p: smallest part size (Default value = 1)
    :type min_p: int
    :param max_p: largest part size (Default value = None)
    :type max_p: int

    .. docstring::python

        >>> list(partitions_gen(4))
        [(4,), (1, 3), (1, 1, 2), (1, 1, 1, 1), (2, 2)]
        >>> list(partitions_gen(4, min_p=1, max_p=2))
        [(1, 1, 2), (1, 1, 1, 1), (2, 2)]

    """
    if max_p is None or max_p >= numero:
        yield (numero,)

    for i in range(min_p, numero // 2 + 1):
        for p in partitions_gen(numero - i, i, max_p):
            yield (i,) + p


@cash_it
def rfactorial(n: int) -> int:
    """Recursive factorial function

    :param n:

    .. docstring::python

        >>> from math import factorial
        >>> rfactorial(1) == factorial(1)
        True
        >>> rfactorial(2) == factorial(2)
        True
        >>> rfactorial(3) == factorial(3)
        True
        >>> rfactorial(4) == factorial(4)
        True
        >>> rfactorial(5) == factorial(5)
        True
        >>> rfactorial(6) == factorial(6)
        True
        >>> rfactorial(7) == factorial(7)
        True
        >>> rfactorial(8) == factorial(8)
        True
        >>> rfactorial(9) == factorial(9)
        True


    """
    if n == 1:
        return 1
    else:
        return rfactorial(n - 1) * n


def radians_2_degrees(rads: float) -> float:
    """Converts radians to degrees

    :param rads:

    .. doctest:: python

        >>> from math import pi
        >>> radians_2_degrees(2*pi) == 360.0
        True
        >>> radians_2_degrees(2*pi)
        360.0


    """
    return 180 * rads / pi


def degrees_2_radians(degs: float) -> float:
    """Converts degrees to radians

    :param degs:

    .. doctest:: python

        >>> from math import pi
        >>> degrees_2_radians(360.0) == 2*pi
        True

    """
    return degs * pi / 180


def power_mod(number: int, exponent: int, mod: int) -> int:
    """

    :param number:
    :param exponent:
    :param mod:

    .. doctest:: python

        >>> power_mod(2, 4, 3)
        2
        >>> power_mod(12, 3, 4)
        144
        >>> power_mod(123, 2, 3)
        123
        >>> power_mod(120, 6, 10)
        14400
        >>> power_mod(120, 6, 1)
        14400

    """
    if exponent > 0:
        if exponent % 2 == 0:
            return power_mod(number, floordiv(exponent, 2), mod)
        return power_mod(number, floordiv(exponent, 2), mod) * number
    else:
        return 1


def divisors_gen(n: int) -> Iterator[int]:
    """Divisors generator

    :param n: number w/ divisors to be generated
    :type n: int

    .. doctest:: python

        >>> list(divisors_gen(1))
        [1]
        >>> list(divisors_gen(4))
        [1, 2, 4]
        >>> list(divisors_gen(16))
        [1, 2, 4, 8, 16]


    """
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


def gcd_it(a: int, b: int) -> int:
    """iterative gcd

    :param a:
    :param b:


        >>> from pupy.maths import gcd_it
        >>> from pupy.maths import gcd_r
        >>> gcd_it(1, 4) == gcd_r(1, 4)
        True
        >>> gcd_it(2, 6) == gcd_r(2, 6)
        True
        >>> gcd_it(3, 14) == gcd_r(3, 14)
        True
        >>> gcd_it(4, 300) == gcd_r(4, 300)
        True

    """
    while a:
        a, b = b % a, a
    return b


@cash_it
def gcd_r(a: int, b: int) -> int:
    """recursive greatest common divisor

    :param a:
    :param b:

    .. doctest:: python

        >>> from pupy.maths import gcd_it
        >>> from pupy.maths import gcd_r
        >>> gcd_it(1, 4) == gcd_r(1, 4)
        True
        >>> gcd_it(2, 6) == gcd_r(2, 6)
        True
        >>> gcd_it(3, 14) == gcd_r(3, 14)
        True
        >>> gcd_it(4, 300) == gcd_r(4, 300)
        True

    """
    if b > a:
        return gcd_r(b, a)
    r = a % b
    if r == 0:
        return b
    return gcd_r(r, b)


def reverse(n: int) -> int:
    """Reverses a number

    :param n: number to be reversed
    :type n: int
    :returns: reversed of a number
    :rtype: int

    .. doctest:: python

        >>> reverse(1)
        1
        >>> reverse(12345)
        54321
        >>> reverse(54321)
        12345
        >>> reverse(54321000)
        12345

    """

    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n % 10
        n //= 10
    return reversed


@cash_it
def fib_r(n: int) -> int:
    """Recursively the nth fibonacci number

    :param n: nth fibonacci sequence number
    :type n: int
    :returns: the nth fibonacci number
    :rtype: int

    .. doctest:: python

        >>> fib_r(1)
        1
        >>> fib_r(2)
        2
        >>> fib_r(6)
        13

    """
    return n if n < 3 else fib_r(n - 1) + fib_r(n - 2)


def expo(d: int, n: int) -> int:
    """greatest exponent for a divisor of n

    :param d: divisor
    :type d: int
    :param n: number be divided
    :type n: int
    :returns: number of times a divisor divides n
    :rtype: int

    .. doctest:: python

        >>> expo(100, 2)
        2
        >>> expo(12, 5)
        0
        >>> expo(12, 2)
        2
        >>> expo(160, 4)
        2
        >>> expo(1000, 4)
        1

    """
    if n < d:  # flip
        d, n = n, d
    c = n
    divs = 0
    while c % d == 0:
        c //= d
        divs += 1
    return divs


def pytriple_gen(max_c: int) -> Iterator[Tuple[int, int, int]]:
    """primative pythagorean triples generator

    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s

    :param max_c: max value of c to yeild triples up to
    :type max_c: int

    """
    for real_pts in range(2, int(sqrt(max_c)) + 1, 1):
        for imag_pts in range(real_pts % 2 + 1, real_pts, 2):
            comp = complex(real_pts, imag_pts)
            sqrd = comp * comp
            real = int(sqrd.real)
            imag = int(sqrd.imag)
            if abs(real - imag) % 2 == 1 and gcd_it(imag, real) == 1:
                sea = int((comp * comp.conjugate()).real)
                if sea > max_c:
                    break
                else:
                    yield (imag, real, sea) if real > imag else (real, imag, sea)


def n_permutations_with_replacements(
    it: Union[
        Tuple[int, int, int, int],
        Tuple[int, int, int, int, int, int, int],
        Tuple[int, int, int, int, int],
        Tuple[int, int, int, int, int, int],
    ]
) -> int:
    """

    .. doctest:: python

        >>> n_permutations_with_replacements((1, 2, 3, 4))
        24
        >>> n_permutations_with_replacements((1, 2, 3, 4, 3))
        60
        >>> n_permutations_with_replacements((1, 2, 3, 4, 3, 3))
        120
        >>> n_permutations_with_replacements((1, 2, 3, 4, 3, 4, 4))
        420


    """
    c = Counter(n for n in it)
    a = list(factorial(nc) for nc in c.values())
    return factorial(len(it)) // iter_product(a)


def disjoint(
    a: Union[List[int], List[Union[str, int]]],
    b: Union[List[int], List[Union[str, int]]],
) -> bool:
    """

    :param a:
    :param b:

    .. doctest:: python

        >>> a = [1, 2, 3, 4]
        >>> b = [2, 3, 4, 5]
        >>> disjoint(a, b)
        False
        >>> a = [1, 2, 3, 4]
        >>> b = [5, 6, 7, 8]
        >>> disjoint(a, b)
        True
        >>> a = ['joe', 'frank', 3, 4]
        >>> b = [5, 6, 7, 'frank']
        >>> disjoint(a, b)
        False


    """
    return not any(ae in b for ae in a)


def set_cmp(
    a: Union[Set[int], List[int]], b: Union[Set[int], List[int]]
) -> Tuple[Set[int], Set[int], Set[int]]:
    """Compare the elements of two iterables (a and b)

    :param a: first iterable to compare elements of
    :param b: second iterable to compare elements of
    :return: tuple of sets of the form (common elements, in a only, in b only)

    .. doctest::

        >>> a = [n for n in range(6)]
        >>> a
        [0, 1, 2, 3, 4, 5]
        >>> b = list(range(3, 9))
        >>> b
        [3, 4, 5, 6, 7, 8]
        >>> set_cmp(a, b)
        ({3, 4, 5}, {0, 1, 2}, {8, 6, 7})

    """
    if not isinstance(a, set) or not isinstance(b, set):
        return set_cmp(set(a), set(b))
    return a & b, a - b, b - a


def n_choose_r(n, r):
    """

    :param n:
    :param r:

    """
    return factorial(n) // factorial(r) // factorial(n - r)


class Trigon(object):
    """Trigon object composed of three points connected by lines."""

    def __init__(
        self,
        pt1: Union[Tuple[int, int]],
        pt2: Union[Tuple[int, int]],
        pt3: Union[Tuple[int, int]],
    ) -> None:
        self.pt1 = Vuple(pt1)
        self.pt2 = Vuple(pt2)
        self.pt3 = Vuple(pt3)

    @classmethod
    def from_points(cls, pts: List[Tuple[int, int]]):
        """

        :param pts: return:

        """
        if len(pts) == 3:
            return Trigon(*pts)
        if len(pts) == 6:
            it = iter(pts)
            return Trigon(*zip(it, it))

    def __str__(self):
        return "<< {}, {}, {} >>".format(self.pt1, self.pt2, self.pt3)

    def __contains__(self, point: Union[Tuple[int, int]]) -> bool:
        if type(point) is not Vuple:
            point = Vuple(point)
        return self.area() == sum(
            map(methodcaller("area"), self.inner_triangles(point))
        )

    def inner_triangles(self, point):
        """Triangle funk that returns the three triangles w/ a point

        The point (p) is connected to each point of a triangle. with points,
        a, b, and c. The three triangles are t1=(a, b, p), t2=(a, c, p), and
        t3 = (b, c, p).

        :param point: point to connect to Triangle Vertices
        :type point: tuple or Vuple
        :returns: t1, t2, t3-> Three triangles

        """
        t1 = Trigon(point, self.pt2, self.pt3)
        t2 = Trigon(self.pt1, point, self.pt3)
        t3 = Trigon(self.pt1, self.pt2, point)
        return t1, t2, t3

    def is_perimeter_point(self, point: Tuple[int, int]) -> bool:
        """

        :param point:

        """
        if type(point) is not Vuple:
            point = Vuple(point)
        return any(
            tri_area == 0
            for tri_area in map(methodcaller("area"), self.inner_triangles(point))
        )

    def points(self):
        """ """
        return self.pt1, self.pt2, self.pt3

    def contains_origin(self) -> bool:
        """True if the origin (0,0) lies within the Triangle"""
        return (0, 0) in self

    def area(self) -> float:
        """ """
        return abs(truediv(Vuple.cross(self.pt1 - self.pt2, self.pt3 - self.pt2), 2))

    @staticmethod
    def area_from_points(pt1, pt2, pt3):
        """

        :param pt1:
        :param pt2:
        :param pt3:

        """
        return abs(truediv(Vuple.cross(pt1 - pt2, pt3 - pt2), 2))


class Vuple(tuple):
    """VUPLE == Vector+Tuple"""

    def __new__(cls: Type[Any], *args) -> Any:
        """

        :param args:
        :return:
        """
        return super(Vuple, cls).__new__(cls, tuple(*args))

    def __gt__(self, other: Any) -> bool:
        return Vuple.mag_sqrd(self) > Vuple.mag_sqrd(other)

    def __eq__(self, other: Union[Tuple[float, float], Tuple[int, int], Any]) -> bool:
        return all(a == b for a, b in zip(self, other))

    def __add__(self, k: Union[int, Any]) -> Any:
        """

        .. docstring::python

            >>> va = Vuple((8, 13))
            >>> vb = Vuple((26, 7))
            >>> va + vb
            (34, 20)

        """
        if type(k) is int or type(k) is float:
            return Vuple((k + el for el in self))
        elif type(k) is Vuple and len(self) == len(k):
            return Vuple(map(add, self, k))
        raise ValueError("huh idk")

    def __iadd__(self, k):
        return self.__add__(k)

    def __sub__(self, k: Any) -> Any:
        return Vuple(map(sub, self, k))

    def __isub__(self, k):
        return self.__sub__(k)

    def __mul__(self, k: Union[int, Any]) -> Union[int, Any]:
        """Multiply by a scalar for each element or cross product if also iterable of same length

        :param k: scalar ot other iterable to do the cross producting with
        :return: A Vuple or a sum as a cost product

        .. docstring::python

            >>> a = Vuple((1, 2, 3))
            >>> a * a
            14
            >>> a = Vuple((1, 1, 1))
            >>> a * 4
            (4, 4, 4)

        """

        if type(k) is int or type(k) is float:
            return self._mul_scalar(k)
        elif type(k) is Vuple:
            if len(k) != len(self):
                raise ValueError("Sizes do not match!")
            return Vuple.dot(self, k)

    def __imul__(self, k: int) -> Any:
        return self.__mul__(k)

    def _mul_scalar(self, k: int) -> Any:
        """

        :param k:

        """
        return Vuple((k * el for el in self))

    def __truediv__(self, k: Union[int, float]) -> Any:
        if type(k) is int or type(k) is float:
            return self._truediv_scalar(k)

    def _truediv_scalar(self, k: Union[int, float]) -> Any:
        """

        :param k:

        """
        return Vuple((el / k for el in self))

    def __itruediv__(self, k: int) -> Any:
        return self.__truediv__(k)

    def __floordiv__(self, k):
        if type(k) is int or type(k) is float:
            return self._floordiv_scalar_int(k)

    def __ifloordiv__(self, k):
        return self.__floordiv__(k)

    def _floordiv_scalar_int(self, k):
        """

        :param k:

        """
        return Vuple((el // k for el in self))

    def normalize(self) -> Any:
        """Normalizes the Vuple ST self.magnitude == 1

        :return: Unit Vuple


        """
        return Vuple.unit_vuple(self)

    @staticmethod
    def unit_vuple(voop: Any) -> Any:
        """

        :param voop:

        """
        return Vuple(voop) / Vuple.mag(voop)

    def get_mag_sqrd(self):
        """ """
        return Vuple.mag_sqrd(self)

    @staticmethod
    def mag_sqrd(voop: Union[Tuple[int, int], Any]) -> int:
        """

        :param voop:

        """
        return sum(el * el for el in voop)

    def get_mag(self) -> float:
        """ """
        return Vuple.mag(self)

    @staticmethod
    def mag(voop: Union[Tuple[int, int], Any]) -> float:
        """

        :param voop:

        .. docstring::python

            >>> v = Vuple((3, 4, 5))

        """
        return sqrt(Vuple.mag_sqrd(voop))

    @staticmethod
    def dot(a: Any, b: Any) -> Union[int, float]:
        """

        :param a:
        :param b:

        """
        return sum(va * vb for va, vb in zip(a, b))

    @staticmethod
    def cross(v1: Any, v2: Any) -> int:
        """Cross product of two 2d vectors

        :param v1: first vector
        :param v2: second vector
        :returns: cross product of v1 and v2

        """
        if len(v1) == 2 and len(v2) == 2:
            return (v1[0] * v2[1]) - (v1[1] * v2[0])
        else:
            raise ValueError("cross product gt 2d not implemented")

    @staticmethod
    def angle(v1: Any, v2: Any, radians: bool = False) -> float:
        """

        :param v1:
        :param v2:
        :param radians:  (Default value = False)

        """
        # return acos(Vuple.dproduct(v1, v2)/(Vuple.mag(v1)*Vuple.mag(v2)))
        q = 1 if radians else 180 / pi
        return q * acos(Vuple.dot(Vuple.unit_vuple(v1), Vuple.unit_vuple(v2)))

    def is_disjoint(self, them):
        """

        :param them:

        """
        return disjoint(self, them)

    def product(self) -> int:
        """Multiplies all elements in the Vuple

        :return:

        .. doctest:: pythonm

            >>> v = Vuple((1, 2, 3, 4))
            >>> v.product()
            24
            >>> v = Vuple((100, 1, -1, 2))
            >>> v.product()
            -200
            >>> v = Vuple((100, -1, -1, 2))
            >>> v.product()
            200


        """
        return iter_product(self)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
