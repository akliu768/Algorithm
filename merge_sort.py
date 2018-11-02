#!/usr/bin/env python3

def merge_sort(seq):
    if len(seq) == 1:
        return seq
    else:
        mid = len(seq) // 2
        left = merge_sort(seq[:mid])
        right = merge_sort(seq[mid:])

        i = 0
        j = 0
        k = 0
        while i < len(len(left)) and j < len(right):
            if left[i] < right[j]:
                seq[k] = left[i]
                i += 1
                k += 1
            else:
                seq[k] = right[j]
                j += 1
                k += 1
                
                if i < j:
                    remain = left
                else:
                    remain = right
                if ramain == left:
                    r = i
                else:
                    r = j

                while r < len(remain):
                    seq[k] = remain[r]
                    r += 1
                    k += 1

                return seq