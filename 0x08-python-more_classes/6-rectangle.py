#!/usr/bin/python3
""" This module defines a class named ``Rectangle``
"""


class Rectangle:
    """ an class named Rectangle that's defined with width
    and height private attributes.
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """This method initializes an instance of ``Rectangle`` class
        Args:
            width (int): the width of rectangle, 0 if not provided.
            height (int): the height of rectangle, 0 if not provided.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """This public instance method returns the area of a Rectangle Object.
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """This public instance method returns the perimeter of a
        Rectangle Object.
        """
        if (self.__height == 0) or (self.__width == 0):
            return (0)
        return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """This method prints the rectangle with character ``#``.
        """
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        recstr = ""
        for i in range(self.__height):
            for j in range(self.__width):
                recstr += "#"
            if (i != ((self.__height) - 1)):
                recstr += "\n"
        return recstr

    def __repr__(self):
        """This method returns a string representation of the rectangle to be
        able to recreate a new instance using eval()
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """This method prints a message when an object is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
