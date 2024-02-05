#!/usr/bin/python3
"""This module defines the class BaseGeometry.
"""


class BaseGeometry:
    """This is an empty class
    """
    def area(self):
        """This method raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value and raises errors
        if value is invalid.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
