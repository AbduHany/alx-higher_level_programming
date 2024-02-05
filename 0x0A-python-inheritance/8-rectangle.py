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
        Args:
            name (str): the name of the value being validated.
            value (int): the value that's being validated.
        Raises:
            TypeError if value isn't ints.
            ValueError if value isn't more than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class represents a rectangle and is inherited from the
    BaseGeometry class.
    """

    def __init__(self, width, height):
        """This method initializes a Rectangle object after checking
        the value of the width and height using the parent class'
        integer_validator method.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        Raises:
            TypeError if width/height aren't ints.
            ValueError if width/height aren't more than 0.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
