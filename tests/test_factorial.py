# -*- coding:utf-8 -*-

from das.algo import factorial

EXAMPLES = [
    (-2, 1),
    (-1, 1),
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
]


def test_factorial_rec():
    for i, o in EXAMPLES:
        assert factorial.factorial_rec(i) == o, "f(%s)=%s" % (i, o)


def test_factorial_acc():
    for i, o in EXAMPLES:
        assert factorial.factorial_acc(i) == o, "f(%s)=%s" % (i, o)


def test_factorial_gen():
    fn = factorial.factorial_gen()
    for i, o in filter(lambda t: t[0] >= 1, EXAMPLES):
        assert next(fn) == o, "f(%s)=%s" % (i, o)
