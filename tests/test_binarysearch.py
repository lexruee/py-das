# -*- coding:utf-8 -*-

from das.algo import search


EXAMPLES = [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 4, 3),
    ([4, 5, 6, 7, 8, 9, 10], 6, 2)
]


def get_example(n):
    ain, aout = EXAMPLES[n][0], EXAMPLES[n][1]
    return ain[:], aout[:]


def test_binary_search_rec():
    for array, value, expected in EXAMPLES:
        result = search.binary_search(array, value, rec=True)
        assert result == expected

def test_binary_search_iter():
    for array, value, expected in EXAMPLES:
        result = search.binary_search(array, value, rec=False)
        assert result == expected

