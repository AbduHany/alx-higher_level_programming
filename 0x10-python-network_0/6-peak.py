#!/usr/bin/python3
"""This module defines the function `find_peak`
"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): list of the unsorted integers.
    Returns:
        the peak integer of the list.
    """
    li = list_of_integers
    if li == []:
        return None
    length = len(li)
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
