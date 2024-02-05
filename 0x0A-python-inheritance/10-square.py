#!/usr/bin/python3
"""This module defines the class ``Square`` that is inherited
_from the Rectangle class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square object and is
    inherited from the Rectangle class.
    """
    def __init__(self, size):
        """This method instantiates the Square
        object
        Args:
            size (int): the size of the square object.
        Raises:
            TypeError: if size isn't an int.
            ValueError: if size isn't bigger than 0.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
