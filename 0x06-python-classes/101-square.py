#!/usr/bin/python3
"""
This module defines the class named Square that defines a square.
"""


class Square:
    """
    This is an empty class named Square that defines a square.
    """

    resultstring = []

    def __init__(self, size=0, position=(0, 0)):
        """
        This method initiates an object instance of class Square.
        Args:
            size (int): size of the square to be initiated.
            position (tuple): position to start printing from.
        """
        self.size = size
        self.position = position
        self.inittable()

    def inittable(self):
        """Initializes the resulttable"""
        self.resultstring = []
        if (self.__size == 0):
            self.resultstring.append("\n")
        else:
            hoff = self.__position[0]
            voff = self.__position[1]
            num = self.__size
            for i in range(voff):
                self.resultstring.append("\n")
            for i in range(num):
                for k in range(hoff):
                    self.resultstring.append(" ")
                for j in range(num):
                    self.resultstring.append("#")
                if (i != (num - 1)):
                    self.resultstring.append("\n")

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
            hoff = self.__position[0]
            voff = self.__position[1]
            num = self.__size
            for i in range(voff):
                print()
            for i in range(num):
                for k in range(hoff):
                    print(" ", end="")
                for j in range(num):
                    print("#", end="")
                print()

    @property
    def size(self):
        """This is the getter method for the private attribute size."""
        return self.__size

    @property
    def position(self):
        """ This is the getter method for the private attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is the setter method for the position private attribute after
        checking the tuple's values and length.

        Args:
            value (tuple): the tuple to be tested before being assigned
            to the position attribute
        """
        if value:
            if ((type(value) is tuple) and (len(value) == 2) and
                    (type(value[0]) is int) and (value[0] >= 0) and
                    (type(value[1]) is int) and (value[1] >= 0)):
                self.__position = value
            else:
                a = "position must be a tuple of 2 positive integers"
                raise TypeError(a)
        else:
            self.__position = (0, 0)

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

    def __str__(self):
        return ("".join(self.resultstring))
