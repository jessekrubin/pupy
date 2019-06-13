# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from typing import Any, Iterator, List

def yesno(question: Any, default: bool = ..., tries: int = ...): ...
def term_table(strings: List[str], row_wise: bool=..., filler: str=...) -> Iterator[Any]: ...