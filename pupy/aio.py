# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python
"""
===========
Async funks
===========
"""
import asyncio
from functools import partial
from functools import wraps

from pupy._jasm import json
from pupy._typing import JASM

try:
    import aiofiles
except ImportError:
    raise ImportError("'pip install aiofiles'..." " if ya wanna use this module!")

try:
    from toml import dumps as toml_dumps
    from toml import load as toml_load
    from toml import loads as toml_loads
except ImportError:
    pass

try:
    from ruamel.yaml import YAML

    _yaml_saver = YAML()
    _yaml_loader = YAML(typ="safe")
except ImportError:
    pass


def asyncify(funk):
    @asyncio.coroutine
    @wraps(funk)
    def afunk(*args, loop=None, executor=None, **kwargs):
        loop = loop if loop else asyncio.get_event_loop()
        pfunc = partial(funk, *args, **kwargs)
        return loop.run_in_executor(executor, pfunc)

    return afunk


async def sabytes(filepath: str, _bytes: bytes) -> None:
    """Read bytes from file path

    :param filepath: filepath as as string to read bites from
    :return: some bytes...
    """
    async with aiofiles.open(filepath, mode="wb") as f:
        await f.write(_bytes)


async def labytes(filepath: str) -> bytes:
    """Read bytes from file path

    :param filepath: filepath as as string to read bites from
    :return: some bytes...
    """
    async with aiofiles.open(filepath, mode="rb") as f:
        _bytes = await f.read()
        return _bytes


async def sastring(filepath: str, string: str) -> None:
    try:
        async with aiofiles.open(filepath, mode="w", encoding="utf-8") as f:
            await f.write(string)
    # except NameError:
    #     raise ImportError("'pip install aiofiles' if ya wanna use this!")
    except UnicodeEncodeError:
        async with aiofiles.open(filepath, mode="w", encoding="latin2") as f:
            await f.write(string)


async def lastring(filepath: str) -> str:
    try:
        async with aiofiles.open(filepath, mode="r", encoding="utf-8") as f:
            _file_string = await f.read()
            return _file_string
    except UnicodeDecodeError:
        async with aiofiles.open(filepath, mode="r", encoding="latin2") as f:
            _file_string = await f.read()
            return _file_string


async def sajson(filepath: str, data: JASM, minify: bool = False) -> None:
    """Save json-serial-ize-able data to a specific filepath.

    :param filepath: destination filepath
    :param data: json cereal-izable dictionary/list/thing
    :param minify: Bool flag -- minify the json file
    :return: None

    """
    if type(data) == dict and any(type(val) == bytes for val in data.values()):
        data = {k: str(v, encoding="utf-8") for k, v in data.items()}
    if minify:
        _json_str = json.dumps(data, ensure_ascii=True)
    else:
        _json_str = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=True)
    await sastring(filepath, _json_str)


async def lajson(filepath: str) -> JASM:
    """Load a json file given a filepath and return the file-data

    :param filepath: path to the jasm file you want to load
    :return: Loaded file contents
    """
    _json_str = await lastring(filepath)
    return json.loads(_json_str)


async def latoml(filepath: str) -> JASM:
    try:
        _toml_str = await lastring(filepath)
        return toml_loads(_toml_str)
    except NameError:
        raise EnvironmentError("'pip install toml' if you wanna use this!")


async def satoml(filepath: str, data: JASM) -> None:
    try:
        filepath = filepath if "." in filepath else "{}.toml".format(filepath)
        _toml_str = toml_dumps(data)
        await sastring(filepath, _toml_str)
    except NameError:
        raise EnvironmentError("'pip install toml' if you wanna use this!")


if __name__ == "__main__":
    pass
    # from doctest import testmod
    # testmod()
