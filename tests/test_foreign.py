from os import path
from shutil import rmtree

from pupy.foreign import dirs_gen
from pupy.foreign import files_gen
from pupy.savings_n_loads import touch


def test_files_gen():
    filepath_parts = [
        ('dir', 'file1.txt'),
        ('dir', 'file2.txt'),
        ('dir', 'file3.txt'),
        ('dir', 'dir2', 'file1.txt'),
        ('dir', 'dir2', 'file2.txt'),
        ('dir', 'dir2', 'file3.txt'),
        ('dir', 'dir2a', 'file1.txt'),
        ('dir', 'dir2a', 'file2.txt'),
        ('dir', 'dir2a', 'file3.txt'),
        ]
    for f in filepath_parts:
        filepath = path.join(*f)
        touch(filepath)
    expected_files = sorted(path.join(*f) for f in filepath_parts)
    files = list(sorted(files_gen('dir')))
    assert expected_files == files
    expected_dirs = sorted(set(path.join(*(part for part in f if '.txt' not in part)) for f in filepath_parts))
    dirs = list(sorted(dirs_gen('dir')))
    assert expected_dirs == dirs
    rmtree('dir')
