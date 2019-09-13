# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import TypeVar
from typing import Union
from typing import cast

Flint = Union[int, float]  # float or int
Paths = Iterable[str]  # iterable of path-strings
JASM = Union[None, bool, int, float, str, List[Any], Dict[str, Any]]  # JSON obj
FuncType = Callable[..., Any]
F = TypeVar("F", bound=FuncType)
