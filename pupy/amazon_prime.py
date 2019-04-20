# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from bisect import bisect
from bisect import bisect_right
from collections.abc import MutableSequence
from itertools import count
from math import sqrt
from typing import Any
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import Union

from pupy.decorations import cash_it
from pupy.maths import divisors_gen


def prime_gen(
    plim: int = 0, kprimes: Union[None, Iterable[int]] = None
) -> Iterator[int]:
    """Infinite (within reason) prime number generator
    
    My big modification is the pdiv_dictionary() function that recreats the
    dictionary of divisors so that you can continue to generate prime numbers
    from a (sorted) list of prime numbers.
    
    Based on:
        eratosthenes by David Eppstein, UC Irvine, 28 Feb 2002
        http://code.activestate.com/recipes/117119/ and the thread at the url

    :param plim: prime_limit; default=0 makes for an infinite generator
    :type plim: int
    :param kprimes: known_primes as an iterable (Default value = None)
    :type kprimes: iter

    .. doctest::

        >>> list(prime_gen(50))
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        >>> list(prime_gen(10))
        [2, 3, 5, 7]

    """

    if kprimes is None:
        kprimes = [2, 3, 5, 7, 11]

    def _dictionary():
        """Recreates the prime divisors dictionary used by the generator"""
        div_dict = {}
        for pdiv in kprimes:
            multiple = kprimes[-1] // pdiv * pdiv
            if multiple % 2 == 0:
                multiple += pdiv
            else:
                multiple += 2 * pdiv
            while multiple in div_dict:
                multiple += pdiv * 2
            div_dict[multiple] = pdiv
        return div_dict

    # [1]
    # See if the upper bound is greater than the known primes
    if 0 < plim <= kprimes[-1]:
        for p in kprimes:
            if p <= plim:
                yield p
        return  # return bc we are done

    # [2]
    # Recreate the prime divisibility dictionary using kprimes;
    # Set start and yield first 4 primes
    divz = _dictionary()
    start = kprimes[-1] + 2  # max prime + 2 (make sure it is odd)
    if start == 13:
        yield 2
        yield 3
        yield 5
        yield 7
        yield 11
    # use count or range depending on if generator is infinite
    it = count(start, 2) if plim == 0 else range(start, plim, 2)
    for num in it:
        prime_div = divz.pop(num, None)
        if prime_div:
            multiple = (2 * prime_div) + num
            while multiple in divz:
                multiple += 2 * prime_div
            divz[multiple] = prime_div
        else:
            divz[num * num] = num
            yield num


def prime_factorization_gen(n: int) -> Iterator[int]:
    """generates all numbers in the prime factorization of n

    :param n: number to be factored
    :type n: int

    .. doctest::

        >>> list(prime_factorization_gen(12))
        [2, 2, 3]
        >>> list(prime_factorization_gen(16))
        [2, 2, 2, 2]

    """
    for factor in prime_factors_gen(n):
        if n <= 1:
            break
        while n % factor == 0:
            n //= factor
            yield factor


def prime_factors_gen(n: int) -> Iterator[Any]:
    """prime factors generator

    :param n: number to be factorized
    :type n: int

    .. doctest:: python

        >>> list(prime_factors_gen(12))
        [2, 3]
        >>> list(prime_factors_gen(16))
        [2]

    """
    return (p for p in divisors_gen(n) if is_prime(p))


@cash_it
def is_prime(number: int) -> bool:
    """Checks if a number is prime

    :param number: number to check if is prime
    :type number: int
    :returns: -> True if number is prime
    :rtype: bool

    .. doctest:: python

        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(5)
        True
        >>> is_prime(6)
        False
        >>> is_prime(7)
        True
        >>> is_prime(100)
        False
        >>> is_prime(89)
        True

    """
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False
    if number < 9:
        return True
    if number % 3 == 0:
        return False
    for step in range(5, int(sqrt(number)) + 1, 6):
        if step >= number:
            break
        if number % step == 0:
            return False
        if number % (step + 2) == 0:
            return False
    return True


class OctopusPrime(MutableSequence):
    """OctopusPrime, the 8-leg autobot, here to help you find PRIMES

    ..
    
        ───────────▄▄▄▄▄▄▄▄▄───────────
        ────────▄█████████████▄────────
        █████──█████████████████──█████
        ▐████▌─▀███▄───────▄███▀─▐████▌
        ─█████▄──▀███▄───▄███▀──▄█████─
        ─▐██▀███▄──▀███▄███▀──▄███▀██▌─
        ──███▄▀███▄──▀███▀──▄███▀▄███──
        ──▐█▄▀█▄▀███─▄─▀─▄─███▀▄█▀▄█▌──
        ───███▄▀█▄██─██▄██─██▄█▀▄███───
        ────▀███▄▀██─█████─██▀▄███▀────
        ───█▄─▀█████─█████─█████▀─▄█───
        ───███────────███────────███───
        ───███▄────▄█─███─█▄────▄███───
        ───█████─▄███─███─███▄─█████───
        ───█████─████─███─████─█████───
        ───█████─████─███─████─█████───
        ───█████─████─███─████─█████───
        ───█████─████▄▄▄▄▄████─█████───
        ────▀███─█████████████─███▀────
        ──────▀█─███─▄▄▄▄▄─███─█▀──────
        ─────────▀█▌▐█████▌▐█▀─────────
        ────────────███████────────────

    
    
    
    """

    def __init__(self, plim: int = 100) -> None:
        # list.__init__(self, list(prime_gen(plim=plim)))
        # super(OctopusPrime, self).__init__()
        p = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]
        if plim == 100:
            self._list = p[:]
        elif plim < 100:
            self._list = list(filter(lambda n: n <= plim, p))
        else:
            self._list = list(prime_gen(plim, p))
        self.max_loaded = self._list[-1]

    def _transform(self, n: Optional[int] = None) -> None:
        """TRANSFORM / grow the list

        :param n:  (Default value = None)

        """
        n = n if n is not None else self._list[-1] * 10
        self._list.extend(list(prime_gen(plim=n, kprimes=self._list)))

    def primes_below(self, upper_bound):
        """Lists primes, p, such that  p < upper_bound

        :param upper_bound: exclusive upper bound
        :type upper_bound: int
        :returns: -> primes less than upper_bound
        :rtype: list

        """
        return self.primes_between(1, upper_bound)

    def primes_between(self, lower_bound: int, upper_bound: int) -> List[int]:
        """Lists primes, p, such that, lower_bound < p < upper_bound

        :param lower_bound: exclusive lower bound
        :type lower_bound: int
        :param upper_bound: exclusive upper bound
        :type upper_bound: int
        :returns: -> primes between lower_bound and upper_bound
        :rtype: list

        """
        if upper_bound > self[-1]:
            self._transform(upper_bound)
        return self[bisect_right(self, lower_bound) : bisect(self, upper_bound)]

    def __len__(self) -> int:
        return len(self._list)

    def __getitem__(self, i: Union[int, slice]) -> Union[int, List[int]]:
        return self._list[i]

    def __delitem__(self, i):
        del self._list[i]

    def __setitem__(self, key, value):
        self._list[key] = value

    def insert(self, index, object):
        """

        :param index: 
        :param object: 

        """
        self._list.insert(index)

    def __str__(self):
        return str(self._list)

    def __repr__(self):
        return str(self._list)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
