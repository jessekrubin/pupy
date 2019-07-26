# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from typing import Any
from typing import Optional

def timestamp(ts: Optional[float] = ...) -> str: ...
def environ_dict(): ...
def linked_tmp_dir(
    suffix: Optional[Any] = ...,
    prefix: Optional[Any] = ...,
    dir: Optional[Any] = ...,
    mkdirs: Any = ...,
    lndirs: Any = ...,
    lnfiles: Any = ...,
) -> None: ...
def prinfo(obj: Any) -> None: ...
