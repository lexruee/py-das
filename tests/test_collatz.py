# -*- coding:utf-8 -*-

from das.algo import collatz

EXAMPLES = [(0, 0), (1, 4), (2, 1), (3, 10), (4, 2), (5, 16)]


def test_collatz_fn():
    for i, o in EXAMPLES:
        assert collatz.collatz_fn(i) == o

def test_collatz_gen():
    fn = collatz.collatz_gen(0)
    for _, o in EXAMPLES:
        assert next(fn) == o

