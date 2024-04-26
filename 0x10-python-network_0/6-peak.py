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
        left = find_peak(li[:half])
        right = find_peak(li[half:])
        return left if left > right else right
