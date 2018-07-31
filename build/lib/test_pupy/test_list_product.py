# coding=utf-8
from __future__ import division, print_function
from time import time
from pupy.decorations import tictoc

l = [i for i in range(1, 100000)]
#
# def _bib_test():
#     from pupy.maths import iter_product
#     ti = time()
#     iter_product(l)
#     te = time()
#     return tictoc.ftime(ti, te)
#
#
# def test_iter_product():
#     print(_bib_test())
#
#
# test_iter_product()
#
# # t = 1
# # for n in l:
# #     t *= n
