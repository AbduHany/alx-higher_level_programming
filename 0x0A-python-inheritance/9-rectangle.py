#!/usr/bin/python3
"""This module defines the class Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """This method returns the area of a Rectangle object
        """
        return (self.__width * self.__height)

    def __str__(self):
        """This method returns the string representation
        for a Rectangle object
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
