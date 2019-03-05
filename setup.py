#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import os
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

from pupy._version import __version__

pupy_vesion = __version__
from itertools import count

with open('pyproject.toml') as f:
    lines = f.read().split('\n')
deps = []
for i in count(1 + lines.index('[tool.poetry.dependencies]')):
    if lines[i] == '':
        break
    try:
        dep = lines[i].split('=')[0].strip(' ')
        if dep not in ('python'):
            deps.append(dep)
    except:
        pass

def read(*names, **kwargs):
    """

    :param names:
    :param kwargs:
    :return:
    """
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
        ) as fh:
        return fh.read()

if 'TOXENV' in os.environ and 'SETUPPY_CFLAGS' in os.environ:
    os.environ['CFLAGS'] = os.environ['SETUPPY_CFLAGS']

setup(
    name='pupy',
    version=pupy_vesion,
    license='BSD 2-Clause License',
    description='Pretty Useful Python',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
        ),
    author='jesse k rubin',
    author_email='jessekrubin@gmail.com',
    url='https://github.com/jessekrubin/pupy',
    repository='https://github.com/jessekrubin/pupy',
    packages=find_packages(include=['pupy'], exclude=['docs', 'tests']),
    py_modules=[splitext(basename(path))[0] for path in glob('./*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
        ],
    keywords=[
        'pretty',
        'useful',
        'tewls'
        ],
    install_requires=deps,
    extras_require={},
    setup_requires=[],
    entry_points={
        'console_scripts': [
            'pupy = pupy.cli:main',
            ]
        },
    cmdclass={},
    ext_modules=[],
    )
