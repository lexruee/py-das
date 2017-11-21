# -*- coding:utf-8 -*-

from das.algo import sort


EXAMPLES = [
    ([3,4,1,2,6,5], [1,2,3,4,5,6])
]


def get_example(n):
    ain, aout = EXAMPLES[n][0], EXAMPLES[n][1]
    return ain[:], aout[:]

def test_insertion_sort():
    ain, aout = get_example(0) 
    assert ain != aout
    sort.insertion_sort(ain)
    assert ain == aout

def test_selection_sort():
    ain, aout = get_example(0) 
    assert ain != aout
    sort.insertion_sort(ain)
    assert ain == aout

def test_merge_sort():
    pass
