# -*- coding: utf-8 -*-
from toml import loads
from pathlib import Path

def get_version():
    path = Path(__file__).resolve().parents[2] / 'pyproject.toml'
    pyproject = loads(open(str(path)).read())
    return pyproject['tool']['poetry']['version']

__version__ = get_version()
