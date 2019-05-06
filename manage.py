# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from os import path
from sys import argv

from argparse import ArgumentParser
from subprocess import run

from pupy.foreign import files_gen
from pupy.savings_n_loads import lstr, sstr
from pupy.utils import path2name

PUPY_HEADER = "# -*- coding: utf-8 -*-\n# ~ Jesse K. Rubin ~ Pretty Useful Python"
CDPATH = path.split(path.abspath(__file__))[0]
SRC_PATH = path.join(CDPATH, 'pupy')
STUBS_PATH = path.join(CDPATH, 'stubs')
TESTS_PATH = path.join(SRC_PATH, 'tests')

def mkstub(filepath):
    run(args=['stubgen', '-o', 'stubs', filepath])

def mkstubs():
    ignore = ['__init__.py', '__main__.py', '_version.py', '_typing.py']
    src_python_files = (fpath for fpath in files_gen(SRC_PATH) if fpath.endswith('.py'))
    src_python_files = [f for f in src_python_files if not any(s in f for s in ignore)]
    for src_file in src_python_files:
        mkstub(src_file)
    stub_files = (fpath for fpath in files_gen(STUBS_PATH) if fpath.endswith('.pyi'))
    for stub in stub_files:
        print(stub)
        stub_name = path2name(stub)
        stub_filepath = path.join(SRC_PATH, stub_name)
        stublimes = lstr(stub).splitlines(keepends=False)[3:]
        stub_file_string = '\n'.join([PUPY_HEADER, *stublimes])
        sstr(stub, stub_file_string)

def cleanup_file(filepath):
    filename = filepath.replace(SRC_PATH, '').strip('\\')
    mkstub(filepath)
    # run(args=['black', filepath])
    # run(args=['isort', '-sl', filepath])

def cleanup_src():
    print("cleaning src")
    print(CDPATH)
    src_python_files = (fpath for fpath in files_gen(SRC_PATH) if fpath.endswith('.py'))
    python_test_files = (fpath for fpath in files_gen(TESTS_PATH) if fpath.endswith('.py'))

    print("PROCESSING SRC CODE")
    for python_file in src_python_files:
        cleanup_file(python_file)

    print("PROCESSING TESTS CODE")
    for python_file in python_test_files:
        cleanup_file(python_file)

def redoc():
    sphinx_args = ['python', '-m', 'sphinx', '-b', 'html', 'docs/', 'docs/_build/']
    run(args=sphinx_args)


def main():
    if len(argv) == 1:
        commands = [
            'python manage.py cleanup                ~  cleanup the src files',
            ]
        print("__SHELDON_MANAGE__")
        print('\n'.join(commands))
        return
    #########
    if 'mkstubs' in argv:
        mkstubs()
    if 'cleanup' in argv:
        cleanup_src()
    if 'redoc' in argv or True:
        redoc()


if __name__ == '__main__':
    main()
