# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from pupy._typing import JASM
from typing import Any

def asyncify(funk: Any): ...
async def sabytes(filepath: str, _bytes: bytes) -> None: ...
async def labytes(filepath: str) -> bytes: ...
async def sastring(filepath: str, string: str) -> None: ...
async def lastring(filepath: str) -> str: ...
async def sajson(filepath: str, data: JASM, minify: bool=...) -> None: ...
async def lajson(filepath: str) -> JASM: ...
async def latoml(filepath: str) -> JASM: ...
async def satoml(filepath: str, data: JASM) -> None: ...