#!/usr/bin/python3
"""This module defines the function `find_peak`
"""


def find_peak(list_of_integers):
    li = list_of_integers
    if li == []:
        return None
    length = len(li)
    print(li, length)
    peak = li[0]
    for i in range(length // 2):
        j = (length - i - 1)
        max = li[i] if li[i] > li[j] else li[j]
        if (max > peak):
            peak = max
    if (length % 2) != 0:
        if li[length//2] > peak:
            peak = li[length//2]
    return (peak)
