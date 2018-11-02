#!/usr/bin/env python3

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    mid = (high + low) // 2
    guess_num = arr[mid]
    if guess_num == item:
        return item
    elif guess_num < item:
        low = mid + 1
    else:
        high = mid - 1
    
    return None