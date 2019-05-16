# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from pupy._typing import JASM

try:
    from aiofiles import open as aopen
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "'pip install aiofiles'..." " if ya wanna use this module!"
    )

try:
    from ujson import dumps
    from ujson import load
    from ujson import loads
except ModuleNotFoundError:
    from json import dumps
    from json import load
    from json import loads

try:
    from toml import dumps as toml_dumps
    from toml import load as toml_load
    from toml import loads as toml_loads
except ModuleNotFoundError:
    pass

try:
    from ruamel.yaml import YAML

    _yaml_saver = YAML()
    _yaml_loader = YAML(typ="safe")
except ModuleNotFoundError:
    pass


async def sabytes(filepath: str, bytes: bytes) -> None:
    """Read bytes from file path

    :param filepath: filepath as as string to read bites from
    :return: some bytes...
    """
    async with aopen(filepath, mode="wb") as f:
        await f.write(bytes)


async def labytes(filepath: str) -> bytes:
    """Read bytes from file path

    :param filepath: filepath as as string to read bites from
    :return: some bytes...
    """
    async with aopen(filepath, mode="rb") as f:
        _bytes = await f.read()
        return _bytes


async def sastring(filepath: str, string: str) -> None:
    try:
        async with aopen(filepath, mode="w", encoding="utf-8") as f:
            await f.write(string)
    # except NameError:
    #     raise ModuleNotFoundError("'pip install aiofiles' if ya wanna use this!")
    except UnicodeEncodeError:
        async with aopen(filepath, mode="w", encoding="latin2") as f:
            await f.write(string)


async def lastring(filepath: str) -> str:
    try:
        async with aopen(filepath, mode="r", encoding="utf-8") as f:
            _file_string = await f.read()
            return _file_string
    except UnicodeDecodeError:
        async with aopen(filepath, mode="r", encoding="latin2") as f:
            _file_string = await f.read()
            return _file_string


async def sajson(filepath: str, data: JASM, min: bool = False) -> None:
    """Save json-serial-ize-able data to a specific filepath.

    :param filepath: destination filepath
    :param data: json cereal-izable dictionary/list/thing
    :param min: Bool flag -- minify the json file
    :return: None

    """
    if type(data) == dict and any(type(val) == bytes for val in data.values()):
        data = {k: str(v, encoding="utf-8") for k, v in data.items()}
    if min:
        _json_str = dumps(data, ensure_ascii=False)
    else:
        _json_str = dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    await sastring(filepath, _json_str)


async def lajson(filepath: str) -> JASM:
    """Load a json file given a filepath and return the file-data

    :param filepath: path to the jasm file you want to load
    :return: Loaded file contents
    """
    _json_str = await lastring(filepath)
    return loads(filepath)


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
