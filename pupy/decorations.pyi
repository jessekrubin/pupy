# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from typing import Any
from typing import Optional

logging_config: Any
logger: Any

def in_n_out(funk: Any): ...

def flog(
    funk: Optional[Any] = ...,
    loglevel: str = ...,
    funk_call: bool = ...,
    tictoc: bool = ...,
    ): ...

def dirdec(funk: Any): ...

def mkdirs(funk: Any): ...

def cash_it(funk: Any): ...

def cprof(funk: Any): ...

def prop(fn: Any): ...

class tictoc:
    runs: Any = ...

    def __init__(self, runs: int = ...) -> None: ...

    args: Any = ...

    def __call__(self, time_funk: Any, printing: bool = ...): ...

def requires(package: Any): ...
