#!/usr/bin/env python3

def binary_search(arr, item):
  low = 0
  high = len(arr) - 1
  mid = (low + high) // 2
  guess_num = arr[mid]
  if guess_num == item:
    return mid
  eiif guess_num < item:
    low = mid + 1
  else:
    high = mid -1
  return NONE
