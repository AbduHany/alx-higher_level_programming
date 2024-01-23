#!/usr/bin/python3
"""
This module defines the class named Square that defines a square.
"""


class Square:
    """
    This is an empty class named Square that defines a square.
    """
    def __init__(self, size=0):
        """
        This method initiates an object instance of class Square.
        Args:
            size (int): size of the square to be initiated.
        """
        if size:
            if type(size) is int:
                if (size > 0):
                    self.__size = size
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        else:
            self.__size = 0

    def area(self):
        """
        This method calculates and returns the area of a square
        Returns:
            int value of the area of the square.
        """
        return (self.__size ** 2)
