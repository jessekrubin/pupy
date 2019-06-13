# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from typing import Any
from typing import Iterator
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import Union

def partitions_gen(
    numero: int, min_p: int = ..., max_p: Optional[int] = ...
) -> Any: ...
def rfactorial(n: int) -> int: ...
def radians_2_degrees(rads: float) -> float: ...
def degrees_2_radians(degs: float) -> float: ...
def power_mod(number: int, exponent: int, mod: int) -> int: ...
def divisors_gen(n: int) -> Iterator[int]: ...
def gcd_it(a: int, b: int) -> int: ...
def gcd_r(a: int, b: int) -> int: ...
def reverse_num(n: int) -> int: ...
def fib_r(n: int) -> int: ...
def expo(d: int, n: int) -> int: ...
def pytriple_gen(max_c: int) -> Iterator[Tuple[int, int, int]]: ...
def n_permutations_with_replacements(
    it: Union[
        Tuple[int, int, int, int],
        Tuple[int, int, int, int, int, int, int],
        Tuple[int, int, int, int, int],
        Tuple[int, int, int, int, int, int],
    ]
) -> int: ...
def disjoint(
    a: Union[List[int], List[Union[str, int]]],
    b: Union[List[int], List[Union[str, int]]],
) -> bool: ...
def set_cmp(
    a: Union[Set[int], List[int]], b: Union[Set[int], List[int]]
) -> Tuple[Set[int], Set[int], Set[int]]: ...
def n_choose_r(n: Any, r: Any): ...

class Trigon:
    pt1: Any = ...
    pt2: Any = ...
    pt3: Any = ...
    def __init__(
        self,
        pt1: Union[Tuple[int, int]],
        pt2: Union[Tuple[int, int]],
        pt3: Union[Tuple[int, int]],
    ) -> None: ...
    @classmethod
    def from_points(cls: Any, pts: List[Tuple[int, int]]) -> Any: ...
    def __contains__(self, point: Union[Tuple[int, int]]) -> bool: ...
    def inner_triangles(self, point: Any): ...
    def is_perimeter_point(self, point: Tuple[int, int]) -> bool: ...
    def points(self): ...
    def contains_origin(self) -> bool: ...
    def area(self) -> float: ...
    @staticmethod
    def area_from_points(pt1: Any, pt2: Any, pt3: Any): ...

class Vuple(tuple):
    def __new__(cls: Type[Any], *args: Any) -> Any: ...
    def __gt__(self, other: Any) -> bool: ...
    def __eq__(
        self, other: Union[Tuple[float, float], Tuple[int, int], Any]
    ) -> bool: ...
    def __add__(self, k: Union[int, Any]) -> Any: ...
    def __iadd__(self, k: Any): ...
    def __sub__(self, k: Any) -> Any: ...
    def __isub__(self, k: Any): ...
    def __mul__(self, k: Union[int, Any]) -> Union[int, Any]: ...
    def __imul__(self, k: int) -> Any: ...
    def __truediv__(self, k: Union[int, float]) -> Any: ...
    def __itruediv__(self, k: int) -> Any: ...
    def __floordiv__(self, k: Any): ...
    def __ifloordiv__(self, k: Any): ...
    def normalize(self) -> Any: ...
    @staticmethod
    def unit_vuple(voop: Any) -> Any: ...
    def get_mag_sqrd(self): ...
    @staticmethod
    def mag_sqrd(voop: Union[Tuple[int, int], Any]) -> int: ...
    def get_mag(self) -> float: ...
    @staticmethod
    def mag(voop: Union[Tuple[int, int], Any]) -> float: ...
    @staticmethod
    def dot(a: Any, b: Any) -> Union[int, float]: ...
    @staticmethod
    def cross(v1: Any, v2: Any) -> int: ...
    @staticmethod
    def angle(v1: Any, v2: Any, radians: bool = ...) -> float: ...
    def is_disjoint(self, them: Any): ...
    def product(self) -> int: ...
