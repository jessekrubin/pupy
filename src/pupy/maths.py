#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from __future__ import division
from __future__ import print_function

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

from pupy.decorations import cash_it
from pupy.foreign import iter_product


def partitions_gen(numero, min_p=1, max_p=None):
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
def rfactorial(n):
    """Recursive factorial function

    :param n:

    """
    if n == 1:
        return 1
    else:
        return rfactorial(n - 1) * n

def radians_2_degrees(rads):
    """Converts radians to degrees

    :param rads: 

    """
    return 180 * rads / pi

def degrees_2_radians(degs):
    """Converts degrees to radians

    :param degs: 

    """
    return degs * pi / 180

def power_mod(number, exponent, mod):
    """

    :param number: 
    :param exponent: 
    :param mod: 

    """
    if exponent > 0:
        if exponent % 2 == 0:
            return power_mod(number, floordiv(exponent, 2), mod)
        return power_mod(number, floordiv(exponent, 2), mod) * number
    else:
        return 1

def divisors_gen(n):
    """Divisors generator

    :param n: number w/ divisors to be generated
    :type n: int

    """
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def gcd_it(a, b):
    """iterative gcd

    :param a: 
    :param b: 

    """
    while a:
        a, b = b % a, a
    return b

@cash_it
def gcd_r(a, b):
    """recursive greatest common divisor

    :param a: 
    :param b: 

    """
    if b > a:
        return gcd_r(b, a)
    r = a % b
    if r == 0:
        return b
    return gcd_r(r, b)

def reverse(n):
    """Reverses a number

    :param n: number to be reversed
    :type n: int
    :returns: reversed of a number
    :rtype: int

    """

    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n % 10
        n //= 10
    return reversed

@cash_it
def fib_r(n):
    """Recursively the nth fibonacci number

    :param n: nth fibonacci sequence number
    :type n: int
    :returns: the nth fibonacci number
    :rtype: int

    .. docstring::python

        >>> fib_r(1)
        1
        >>> fib_r(2)
        2
        >>> fib_r(6)
        13

    """
    return n if n < 3 else fib_r(n - 1) + fib_r(n - 2)

def expo(d, n):
    """greatest exponent for a divisor of n

    :param d: divisor
    :type d: int
    :param n: number be divided
    :type n: int
    :returns: number of times a divisor divides n
    :rtype: int

    """
    if n < d:  # flip
        d, n = n, d
    c = n
    divs = 0
    while c % d == 0:
        c //= d
        divs += 1
    return divs

def pytriple_gen(max_c):
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

def repermutations(toop):
    """

    :param toop: 

    """
    c = Counter(n for n in toop)
    a = list(factorial(nc) for nc in c.values())
    ans = factorial(len(toop)) // iter_product(a)
    return ans

def disjoint(a, b):
    """

    :param a: 
    :param b: 

    """
    return not any(ae in b for ae in a)

def n_choose_r(n, r):
    """

    :param n: 
    :param r: 

    """
    return factorial(n) // factorial(r) // factorial(n - r)

def pytriple_gen_2():
    """ """
    diagonal_size = 3
    cur_x = 1
    cur_y = 2
    while True:
        if cur_y <= cur_x:
            diagonal_size += 1
            cur_x = 1
            cur_y = diagonal_size - 1
        imag_part = cur_y
        real_part = cur_x
        to_yield = get_pythag_triple(real_part, imag_part)
        cur_x += 1
        cur_y -= 1
        if gcd_it(to_yield[0], to_yield[1]) > 1:
            continue
        yield to_yield

def get_pythag_triple(real, imag):
    """

    :param real: 
    :param imag: 

    """
    comp = complex(real, imag)
    sea = int((comp * comp.conjugate()).real)
    sqrd = comp * comp
    real = abs(int(sqrd.real))
    imag = abs(int(sqrd.imag))
    return min(imag, real), max(imag, real), sea

class Trigon(object):
    """Trigon object composed of three points connected by lines."""

    def __init__(self, pt1, pt2, pt3):
        self.pt1 = Vuple(pt1)
        self.pt2 = Vuple(pt2)
        self.pt3 = Vuple(pt3)
    @classmethod
    def from_points(cls, pts):
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
    def __contains__(self, point):
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
    def is_perimeter_point(self, point):
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
    def contains_origin(self):
        """True if the origin (0,0) lies within the Triangle"""
        return (0, 0) in self
    def area(self):
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

    def __new__(cls, *args):
        """

        :param args:
        :return:
        """
        return super(Vuple, cls).__new__(cls, tuple(*args))
    def __gt__(self, other):
        return Vuple.mag_sqrd(self) > Vuple.mag_sqrd(other)
    def __eq__(self, other):
        return all(a == b for a, b in zip(self, other))
    def __add__(self, k):
        """

        .. docstring::python

            >>> va = Vuple((8, 13))
            >>> vb = Vuple((26, 7))
            >>> va + vb
            (34, 20)

        """
        if type(k) is int or type(k) is float:
            return Vuple((k + el for el in self))
        elif type(k) is Vuple:
            if len(self) != len(k):
                raise ValueError("Dimensions do NOT match")
            return Vuple(map(add, self, k))
    def __iadd__(self, k):
        return self.__add__(k)
    def __sub__(self, k):
        return Vuple(map(sub, self, k))
    def __isub__(self, k):
        return self.__sub__(k)
    def __mul__(self, k):
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
    def __imul__(self, k):
        return self.__mul__(k)
    def _mul_scalar(self, k):
        """

        :param k: 

        """
        return Vuple((k * el for el in self))
    def __truediv__(self, k):
        if type(k) is int or type(k) is float:
            return self._truediv_scalar(k)
    def _truediv_scalar(self, k):
        """

        :param k: 

        """
        return Vuple((el / k for el in self))
    def __itruediv__(self, k):
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
    def normalize(self):
        """Normalizes the Vuple ST self.magnitude == 1
        
        :return: Unit Vuple


        """
        return Vuple.unit_vuple(self)
    @staticmethod
    def unit_vuple(voop):
        """

        :param voop: 

        """
        return Vuple(voop) / Vuple.mag(voop)
    def get_mag_sqrd(self):
        """ """
        return Vuple.mag_sqrd(self)
    @staticmethod
    def mag_sqrd(voop):
        """

        :param voop: 

        """
        return sum(el * el for el in voop)
    def get_mag(self):
        """ """
        return Vuple.mag(self)
    @staticmethod
    def mag(voop):
        """

        :param voop:

        .. docstring::python

            >>> v = Vuple((3, 4, 5))

        """
        return sqrt(Vuple.mag_sqrd(voop))
    @staticmethod
    def dot(a, b):
        """

        :param a: 
        :param b: 

        """
        return sum(va * vb for va, vb in zip(a, b))
    @staticmethod
    def cross(v1, v2):
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
    def angle(v1, v2, radians=False):
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
        return len(set(self) & set(them)) == 0
    def product(self):
        """Multiplies all elements in the Vuple
        
        :return:


        """
        return iter_product(self)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
