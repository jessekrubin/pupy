# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from pathlib import Path

__version__ = (
    [
        l
        for l in open(str(Path(__file__).resolve().parents[1] / "pyproject.toml"))
        .read()
        .split("\n")
        if "version" in l
    ][0]
    .replace("version = ", "")
    .strip('"')
)
