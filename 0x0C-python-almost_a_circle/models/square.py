#!/usr/bin/python3
"""This module defines the class ``Square``.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a Square class that's inherited from
    the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """This method instantiates a Square object with the attributes
        size, x, y, and id.
        Args:
            size (int): the size of a square object.
            x (int): The x offset of a square object.
            y (int): the y offset of a square object.
            id (int): the id of a square object.
        """
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """This method prints a string representation of a Square object.
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.height))
