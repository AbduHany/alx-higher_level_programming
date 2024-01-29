#!/usr/bin/python3
"""
This module contains a function that adds 2 elements together.
after typecasting them to ints and raising errors if encountered.
The default value of int b is 98 if not given.
"""


def add_integer(a, b=98):
    """
    This function adds 2 integers and returns their sum.
    """
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
