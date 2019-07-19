# def sync
import asyncio
from concurrent.futures import ThreadPoolExecutor
from os import lstat
from os import mkdir

import aiofiles

from pupy.aio import asyncify
from pupy.foreign import dirs_gen
from pupy.foreign import files_gen

lstat = asyncify(lstat)


def sstr(filepath, string):
    with open(filepath, 'wb') as f:
        f.write(string)


asstring = asyncify(sstr)


async def read_in_chunks(file_object, chunk_size=4096):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


async def _cp_files(src_filepath, dest_filepath):
    async with aiofiles.open(src_filepath, 'rb') as sf:
        content = await sf.read()
        await asstring(dest_filepath, content)

        # async with aiofiles.open(dest_filepath, 'wb') as df:
        #     await df.write(content)


async def _sync_files(src_filepath, dest_filepath):
    # print('----------')
    # print('src', src_filepath)
    # print('dst', dest_filepath)
    # _cp_files(src_filepath, dest_filepath)
    try:
        dest_lstat = await lstat(dest_filepath)

    except FileNotFoundError:
        await _cp_files(src_filepath, dest_filepath)
        return

    src_lstat = await lstat(src_filepath)
    print('lstat src', src_lstat)
    print('lstat dest', dest_lstat)


async def _sync(src, dest):
    dirs = ((dirpath, dirpath.replace(src, dest))
            for dirpath in dirs_gen(src, abspath=True))
    for srcdirpath, destdirpath in dirs:
        try:
            mkdir(destdirpath)
        except FileExistsError:
            pass

    filepaths = ((filepath, filepath.replace(src, dest))
                 for filepath in files_gen(src, abspath=True))

    for src_filepath, dest_filepath in filepaths:
        # print(src_filepath)
        await _sync_files(src_filepath, dest_filepath)


def sync(src, dest):
    loop = asyncio.get_event_loop()
    p = ThreadPoolExecutor()
    loop.run_until_complete(_sync(src, dest))


from pupy import sh
from time import time
from shutil import rmtree


def resetthingy(dir):
    try:
        rmtree(dir)
    except:
        pass
    try:
        mkdir(dir)
    except:
        pass


resetthingy('./docs_2')
resetthingy('./docs_3')
# import sys
# sys.exit()
ta = time()
sync('./docs', './docs_2')
tb = time()
print("done uno", tb - ta)
tc = time()
sh.LIN.sync('./docs', './docs_3')
td = time()
print(td - tc)

from subprocess import run

print('diffing')
run(['diff', '-r', 'docs_2', 'docs_3'])
