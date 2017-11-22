# -*- coding:utf-8 -*-

from das.algo import gcd


EXAMPLES = [
    (15, 6, 3),
    (6, 15, 3),
    (100, 35, 5),
    (35, 100, 5)
]


def get_example(n):
    a, b, d = EXAMPLES[n]
    return a, b, d

def test_gcd_iter1():
    a, b, d = get_example(0) 
    assert gcd.gcd(a, b) == d

def test_gcd_iter2():
    a, b, d = get_example(1) 
    assert gcd.gcd(a, b) == d

def test_gcd_iter3():
    a, b, d = get_example(2) 
    assert gcd.gcd(a, b) == d

def test_gcd_iter4():
    a, b, d = get_example(3) 
    assert gcd.gcd(a, b) == d

def test_gcd_rec1():
    a, b, d = get_example(0) 
    assert gcd.gcd(a, b, True) == d

def test_gcd_rec2():
    a, b, d = get_example(1) 
    assert gcd.gcd(a, b, True) == d

def test_gcd_rec3():
    a, b, d = get_example(2) 
    assert gcd.gcd(a, b, True) == d

def test_gcd_rec4():
    a, b, d = get_example(3) 
    assert gcd.gcd(a, b, True) == d

