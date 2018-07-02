# -*- coding:utf-8 -*-

from das.algo import fermat


NUMBERS = [3, 5, 17, 257, 65537]


def test_fermat_number():
    for i, fnum in zip(range(0, len(NUMBERS)), NUMBERS):
        assert fermat.fermat_number(i) == fnum

def test_fermat_numbers():
    for fn in fermat.fermat_numbers(5):
        assert fn in NUMBERS
