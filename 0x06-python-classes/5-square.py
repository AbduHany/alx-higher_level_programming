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
        self.size = size

    def area(self):
        """
        This method calculates and returns the area of a square
        Returns:
            int value of the area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints in stdout the square with the character #. """
        if (self.__size == 0):
            print()
        else:
            num = self.__size
            for i in range(num):
                for j in range(num):
                    print("#", end="")
                print()
            print()

    @property
    def size(self):
        """This is the getter method for the private attribute size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        This setter method sets the value of private attribute size after
        checking its value and type.

        Args:
            value (int): the value to be tested before assigning it to the
            prive attribute size.
        """
        if value:
            if type(value) is int:
                if (value > 0):
                    self.__size = value
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
        else:
            self.__size = 0
