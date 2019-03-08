# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from typing import Any
from typing import Generator
from typing import Iterable
from typing import List
from typing import Sequence
from typing import Union

Flint = Union[int, float]

def partitions_gen(numero: int, min_p: int = ..., max_p: int = ...) -> Generator: ...
def rfactorial(n: int): ...
def radians_2_degrees(rads: Flint): ...
def degrees_2_radians(degs: Flint): ...
def power_mod(number: Flint, exponent: Flint, mod: Flint): ...
def divisors_gen(n: int) -> Generator: ...
def gcd_it(a: int, b: int): ...
def gcd_r(a: int, b: int): ...
def reverse(n: int): ...
def fib_r(n: int): ...
def expo(d: Any, n: Any): ...
def pytriple_gen(max_c: int) -> Generator: ...
def repermutations(toop: tuple) -> int: ...
def disjoint(a: Iterable, b: Iterable) -> bool: ...
def n_choose_r(n: int, r: int) -> int: ...
def pytriple_gen_2() -> None: ...
def get_pythag_triple(real: Any, imag: Any): ...

class Trigon:
    pt1: Any = ...
    pt2: Any = ...
    pt3: Any = ...
    def __init__(self, pt1: Any, pt2: Any, pt3: Any) -> None: ...
    @classmethod
    def from_points(cls, pts: List[Any]): ...
    def __str__(self): ...
    def __contains__(self, point: Any): ...
    def inner_triangles(self, point: Any): ...
    def is_perimeter_point(self, point: Any): ...
    def points(self): ...
    def contains_origin(self): ...
    def area(self): ...
    @staticmethod
    def area_from_points(pt1: Any, pt2: Any, pt3: Any): ...

class Vuple(tuple):
    Voops = Union[tuple, int, float, Sequence]
    def __new__(cls, *args: Any): ...
    def __gt__(self, other: Any): ...
    def __eq__(self, other: Any): ...
    def __add__(self, k: Voops): ...
    def __sub__(self, k: Voops): ...
    def __mul__(self, k: Union[tuple, int, float]): ...
    def __imul__(self, k: Union[tuple, int, float]): ...
    def _mul_scalar(self, k: Flint): ...
    def __truediv__(self, k: Voops): ...
    def _truediv_scalar(self, k: Flint): ...
    def __itruediv__(self, k: Voops): ...
    def __floordiv__(self, k: Voops): ...
    def __ifloordiv__(self, k: Voops): ...
    def _floordiv_scalar_int(self, k: Flint): ...
    def normalize(self): ...
    def get_mag_sqrd(self): ...
    def get_mag(self): ...
    def is_disjoint(self, them: Any): ...
    def product(self): ...
    @staticmethod
    def unit_vuple(voop: Union[Vuple, tuple]): ...
    @staticmethod
    def mag_sqrd(voop: Union[Vuple, tuple, List[Union[int, float]]]): ...
    @staticmethod
    def mag(voop: Any): ...
    @staticmethod
    def dot(a: Any, b: Any): ...
    @staticmethod
    def cross(v1: Any, v2: Any): ...
    @staticmethod
    def angle(
        v1: Union[Vuple, tuple], v2: Union[Vuple, tuple], radians: bool = ...
    ): ...
