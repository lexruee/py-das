# -*- coding:utf-8 -*-

__author__ = 'Alexander Rüedlinger'

def selection_sort(array):
    n = len(array)
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if array[j] < array[k]:
                k = j
        if k != i:
            a, b = array[i], array[k]
            array[i], array[k] = b, a

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key 

def merge_sort(array):
    pass
