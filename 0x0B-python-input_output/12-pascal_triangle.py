#!/usr/bin/python3
"""This module defines the function ``pascal_triangle``.
"""


def pascal_triangle(n):
    """This function returns a list of lists of integers representing the
    Pascal's triangle of n
    Args:
        n (int): the number representing the height of the pascal's triangle
    """
    res = []
    if (n <= 0):
        return res

    for i in range(n + 1):
        num = 1
        row = []
        for k in range(1, i + 1):
            row.append(num)
            num = num * (i - k) // k
        if row == []:
            continue
        res.append(row)
    return (res)
