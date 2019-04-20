# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from typing import Any
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Tuple
from typing import Union

from pupy._typing import Flint


def files_gen(dirpath: str = ..., abs: bool = ...) -> Iterator[Any]: ...
def dirs_gen(dirpath: str = ..., abs: bool = ...) -> Iterator[Any]: ...
def exhaust(it: Iterable[Any]) -> None: ...
def chunks(it: Union[List[int], str], chunk_size: int) -> Iterator[Any]: ...
def is_permutation(
    a: Union[int, List[int], str], b: Union[int, List[int], str]
) -> bool: ...
def rotate(rlist: List[int], rn: int = ..., left_rotate: bool = ...) -> List[int]: ...
def rotations_gen(rlist: Tuple[int, int, int, int]) -> Iterator[Any]: ...
def digits_list(number: int) -> List[int]: ...
def int_from_digits(digits: Iterable[int]) -> int: ...
def iter_product(l: Iterable[int]) -> Flint: ...
