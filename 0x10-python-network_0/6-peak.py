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
    if li == [] or li is None:
        return None
    if len(li) == 1:
        return (li[0])
    elif len(li) == 2:
        return (li[0] if li[0] > li[1] else li[1])
    else:
        half = len(li) // 2
        if (li[half] > li[half - 1] and li[half] > li[half + 1]):
            return li[half]
        elif (li[half] < li[half + 1] and li[half] > li[half - 1]):
            return find_peak(li[half:])
        elif (li[half] < li[half - 1] and li[half] > li[half + 1]):
            return find_peak(li[:half])
        else:
            return find_peak(li[:half])
