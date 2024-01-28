#!/usr/bin/python3
"""This module defines a function that prints a square with the char `#`."""


def print_square(size):
    """
    prints a square with the character `#`.
    Args:
        size (int): the size length of the square.
    Raises:
        TypeError: if size isn't an int.
        ValueError: if size if less than 0.
    """
    if (type(size) is not int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (type(size) is float) and (size < 0):
        raise TypeError("size must be an integer")
    for i in range(size):
        print(size * '#')
