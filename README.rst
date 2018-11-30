========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-pupy/badge/?style=flat
    :target: https://readthedocs.org/projects/python-pupy
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/jessekrubin/python-pupy.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/jessekrubin/python-pupy

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/jessekrubin/python-pupy?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/jessekrubin/python-pupy

.. |requires| image:: https://requires.io/github/jessekrubin/python-pupy/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/jessekrubin/python-pupy/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/jessekrubin/python-pupy/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/jessekrubin/python-pupy

.. |codecov| image:: https://codecov.io/github/jessekrubin/python-pupy/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/jessekrubin/python-pupy

.. |version| image:: https://img.shields.io/pypi/v/pupy.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pupy

.. |commits-since| image:: https://img.shields.io/github/commits-since/jessekrubin/python-pupy/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/jessekrubin/python-pupy/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pupy.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pupy

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pupy.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pupy

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pupy.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pupy


.. end-badges

Pretty Useful Python

* Free software: BSD 2-Clause License

Installation
============

::

    pip install pupy

Documentation
=============


https://python-pupy.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
