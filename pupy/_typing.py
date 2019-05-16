# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from typing import Any
from typing import Dict
from typing import Iterable
from typing import List
from typing import Union

Flint = Union[int, float]  # float or int
Paths = Iterable[str]  # iterable of path-strings
JASM = Union[None, bool, int, float, str, List[Any], Dict[str, Any]]  # JSON obj
