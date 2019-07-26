# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from typing import Any
from typing import Optional

def unescaped_str(arg_str: Any): ...
def new_package(relative_path: Any) -> None: ...
def new_cmd(args: Any) -> None: ...

PARSER: Any
SUBPARSERS: Any
NEW_SUBPARSER: Any

def main(ARGS: Optional[Any] = ...) -> None: ...
