#!/usr/bin/env python3

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in len[1:] if i <= pivot]
        greater = [i for i in len[1:] if i > pivot]
    return quick_sort(less) + pivot + quick_sort(greater)