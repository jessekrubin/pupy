#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from __future__ import division
from __future__ import print_function
from __future__ import with_statement

from pupy.amazon_prime import OctopusPrime
from pupy.amazon_prime import is_prime
from pupy.amazon_prime import prime_factorization_gen
from pupy.amazon_prime import prime_factors_gen
from pupy.amazon_prime import prime_gen
from pupy.decorations import Jasm
from pupy.decorations import cash_it
from pupy.decorations import cprof
from pupy.decorations import tictoc
from pupy.foreign import chunks
from pupy.foreign import digits_list
from pupy.foreign import int_from_digits
from pupy.foreign import is_permutation
from pupy.foreign import iter_product
from pupy.foreign import rotate
from pupy.foreign import rotations_gen
from pupy.maths import Trigon
from pupy.maths import Vuple
from pupy.maths import degrees_2_radians
from pupy.maths import disjoint
from pupy.maths import divisors_gen
from pupy.maths import expo
from pupy.maths import fib_r
from pupy.maths import gcd_it
from pupy.maths import gcd_r
from pupy.maths import get_pythag_triple
from pupy.maths import n_choose_r
from pupy.maths import partitions_gen
from pupy.maths import power_mod
from pupy.maths import pytriple_gen
from pupy.maths import radians_2_degrees
from pupy.maths import repermutations
from pupy.maths import reverse
from pupy.maths import rfactorial
from pupy.savings_n_loads import load_jasm
from pupy.savings_n_loads import loads
from pupy.savings_n_loads import safe_path
from pupy.savings_n_loads import save_jasm
from pupy.savings_n_loads import savings
from pupy.werd import binary_string
from pupy.werd import is_palindrome
from pupy.werd import string_score

__version__ = "__version__ = '2.1.3'"

try:
    range
except NameError:
    range = xrange

ALL = (
    "degrees_2_radians",
    "disjoint",
    "divisors_gen",
    "expo",
    "fib_r",
    "gcd_it",
    "gcd_r",
    "get_pythag_triple",
    "n_choose_r",
    "partitions_gen",
    "power_mod",
    "pytriple_gen",
    "radians_2_degrees",
    "repermutations",
    "reverse",
    "rfactorial",
    "Trigon",
    "Vuple",
    "loads",
    "load_jasm",
    "safe_path",
    "save_jasm",
    "savings",
    "is_palindrome",
    "string_score",
    "binary_string",
    "OctopusPrime",
    "prime_gen",
    "prime_factorization_gen",
    "prime_factors_gen",
    "is_prime",
    "tictoc",
    "cprof",
    "cash_it",
    "Jasm",
    "chunks",
    "is_permutation",
    "rotate",
    "rotations_gen",
    "digits_list",
    "int_from_digits",
    "iter_product",
)
__all__ = tuple(sorted(ALL))
