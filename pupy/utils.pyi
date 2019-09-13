# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from pupy._typing import F


def timestamp(ts: Optional[Union[float, datetime]] = ...) -> str: ...
def environ_dict() -> Dict[str, str]: ...
def linked_tmp_dir(
    suffix: Optional[str] = ...,
    prefix: Optional[str] = ...,
    dir: Optional[str] = ...,
    mkdirs: Optional[List[str]] = ...,
    lndirs: Optional[List[Tuple[str, str]]] = ...,
    lnfiles: Optional[List[Tuple[str, str]]] = ...,
) -> Any: ...
def prinfo(obj: Any) -> None: ...
def pyfilepath(split: bool = ...) -> str: ...
def time_funk(funk: F, *args: Any, **kwargs: Any) -> Any: ...
def cmp_funks(
    f1: F, f2: F, runs: int, *args: Any, **kwargs: Any
) -> Dict[str, Union[str, float, int]]: ...
