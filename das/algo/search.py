#!/usr/bin/env python

def search(array, value):
    low, high = 0, len(array)
    
    while low <= high:
        mid = (low + high)//2
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def search_rec(array, value, low, high):
    if high < low:
        return -1

    mid = (low + high)//2
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return search_rec(array, value, mid+1, high)
    else:
        return search_rec(array, value, low, mid-1)


examples = [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5], 4),
    ([4, 5, 6, 7, 8, 9, 10], 6)
]

for array, value in examples:
    result = search(array, value)
    print("result: {}".format(result))

for array, value in examples:
    result = search_rec(array, value, 0, len(array))
    print("result: {}".format(result))

