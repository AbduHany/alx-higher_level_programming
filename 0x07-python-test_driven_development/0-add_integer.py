#!/usr/bin/python3
"""This module contains a function that adds 2 integers together."""

def add_integer(a, b=98):
    """ This function adds 2 integers and returns their sum.

    if only one argument is given, then the function adds this
    input to the default contant 98.

    Args:
        a (int or float): the first integer or float to be added.
        b (int or float): the second integer or float to be added.
    Returns:
        the sum after typecasting a and b to integers.
    """
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
