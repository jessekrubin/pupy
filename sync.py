# -*- coding: utf-8 -*-
from os import lstat
from os import mkdir

from pupy import aio
import aiofiles
import asyncio
from pupy.foreign import dirs_gen
from pupy.foreign import files_gen
from concurrent.futures import ThreadPoolExecutor

async def lstat_async(filepath):
    return await lstat(filepath)

async def read_in_chunks(file_object, chunk_size=4096):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

async def _cp_files(src_filepath, dest_filepath):
    # f = open(src_filepath, 'rb')
    # async with aiofiles.open('filename', mode='r') as f:
    #     contents = await f.read()
    # with open(dest_filepath, 'wb') as df:
    #     async for piece in read_in_chunks(f):
    #         df.write(piece)
    async with aiofiles.open(src_filepath, 'rb') as sf:
        async with aiofiles.open(dest_filepath, 'wb') as df:
            chunk = await sf.read(2048)
            await df.write(chunk)
        # async for piece in read_in_chunks(f):
        #     df.write(piece)

async def _sync_files(src_filepath, dest_filepath):
    print('----------')
    print('src', src_filepath)
    print('dst', dest_filepath)
    # _cp_files(src_filepath, dest_filepath)
    print(lstat(src_filepath))
    try:
        dest_lstat = lstat(dest_filepath)
    except FileNotFoundError:
        await _cp_files(src_filepath, dest_filepath)
        return

    src_lstat = lstat(src_filepath)
    print(dest_lstat, src_lstat)

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
        print(src_filepath)
        await _sync_files(src_filepath, dest_filepath)

def sync(src, dest):
    loop = asyncio.get_event_loop()
    p = ThreadPoolExecutor(4)  # Create a ProcessPool with 2 processes
    loop.run_until_complete(_sync(src, dest))

def dir_diff(src, dest):
    loop = asyncio.get_event_loop()
    p = ThreadPoolExecutor(4)  # Create a ProcessPool with 2 processes
    loop.run_until_complete(_sync(src, dest))



from pupy import sh
from time import time

# ta = time()
# sync('./docs', './docs_2')
# tb = time()
# print("done uno", tb - ta)
# tc = time()
# sh.LIN.sync('./docs', './docs_3')
# td = time()
# print(td - tc)


if __name__ == "__main__":
    pass
    # from doctest import testmod
    # testmod()
