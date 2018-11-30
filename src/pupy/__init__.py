#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from __future__ import print_function, division, with_statement
__version__ = '2.0.0'
try:
    range
except NameError:
    range = xrange
from pupy.amazon_prime import (OctopusPrime,
                               prime_gen,
                               prime_factorization_gen,
                               prime_factors_gen,
                               is_prime, )
from pupy.decorations import (tictoc,
                              cprof,
                              cash_it,
                              Jasm, )
from pupy.listless import (chunks,
                           is_permutation,
                           rotate,
                           rotations_gen,
                           digits_list,
                           int_from_digits,
                           iter_product, )
from pupy.maths import (degrees_2_radians,
                        disjoint,
                        divisors_gen, expo,
                        fib_r,
                        gcd_it,
                        gcd_r,
                        get_pythag_triple,
                        n_choose_r,
                        partitions_gen,
                        power_mod,
                        pytriple_gen,
                        radians_2_degrees,
                        repermutations,
                        reverse,
                        rfactorial,
                        Trigon,
                        Vuple, )
from pupy.savings_n_loads import (load_jasm,
                                  loads,
                                  safe_path,
                                  save_jasm,
                                  savings, )
from pupy.werd import (is_palindrome,
                       string_score,
                       binary_string, )

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
    "iter_product"
)
__all__ = tuple(sorted(ALL))