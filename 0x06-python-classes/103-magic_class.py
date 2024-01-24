#!/usr/bin/python3
"""This module contains the definition of the MagicClass class"""


class MagicClass:
    """This class defines a Magic class"""

    def __init__(self, radius=0):
        """
        This method initializes a MagicClass object
        Args:
            radius (int): the radius of a circle
        """
        if (type(radius) is not int):
            if (type(radius) is not float):
                raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """This method calculates the area of a circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """This method calculates the circumference of a circle"""
        return ((math.pi * 2) * (self.__radius))
