# -*- coding:utf-8 -*-

from das.algo import sort


EXAMPLES = [
    ([3, 4, 1, 2, 6, 5], [1, 2, 3, 4, 5, 6]),
    ([9, 3, 2, 6, 2, 1], [1, 2, 2, 3, 6, 9])
]


def test_insertion_sort():
    for ain, aout in EXAMPLES:
        _ain = ain[:]
        assert _ain != aout
        sort.insertion_sort(_ain)
        assert _ain == aout


def test_selection_sort():
    for ain, aout in EXAMPLES:
        _ain = ain[:]
        assert _ain != aout
        sort.selection_sort(_ain)
        assert _ain == aout


def test_quick_sort():
    for ain, aout in EXAMPLES:
        _ain = ain[:]
        assert _ain != aout
        sort.quick_sort(_ain)
        assert _ain == aout


def test_merge_sort():
    for ain, aout in EXAMPLES:
        _ain = ain[:]
        assert _ain != aout
        r = sort.merge_sort(_ain)
        assert r == aout
