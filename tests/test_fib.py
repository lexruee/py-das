# -*- coding:utf-8 -*-

from das.algo import fib


EXAMPLES = [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55)
]


def test_fib():
    for n, r in EXAMPLES:
        assert fib.fib(n) == r

def test_fib_trec():
    for n, r in EXAMPLES:
        assert fib.fib(n, rec=True) == r

def test_fib_nrec():
    for n, r in EXAMPLES:
        assert fib.fib_nrec(n) == r

def test_fib_mrec():
    for n, r in EXAMPLES:
        assert fib.fib_mrec(n) == r

def test_fib_iter():
    for n, r in EXAMPLES:
        assert fib.fib(n, rec=False) == r
