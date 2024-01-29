#!/usr/bin/python3
""" This module defines a class named ``Rectangle``
"""


class Rectangle:
    """ an class named Rectangle that's defined with width
    and height private attributes.
    """
    def __init__(self, width=0, height=0):
        """This method initializes an instance of ``Rectangle`` class
        Args:
            width (int): the width of rectangle, 0 if not provided.
            height (int): the height of rectangle, 0 if not provided.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is the getter property for private attribute ``width``.
        """
        return self.__width

    @property
    def height(self):
        """This is the getter property for private attribute ``height``.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """This is the setter property for private attribute ``width``.
        Args:
            value (int): the value that attribute ``width`` will be set to
                after being checked if positive and is int.
        Raises:
            TypeError: if value isn't of type ``int``.
            ValueError: if value is less than 0.
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """This is the setter property for private attribute ``height``.
        Args:
            value (int): the value that attribute ``height`` will be set to
                after being checked if positive and is int.
        Raises:
            TypeError: if value isn't of type ``int``.
            ValueError: if value is less than 0.
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
