#!/usr/bin/python3
"""This module defines the class ``Rectangle``.
"""
from models.base import Base


class Rectangle(Base):
    """This class defines the Rectangle object and is inherited
    from the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initiates a Rectangle object.
        Args:
            width (int): the width of a rectangle object.
            height (int): the height of a rectangle object.
            x (int): the x attribute of a retangle object.
            y (int): the y attribute of a rectangle object.
            id (int): the id for the rectangle object.
        Raises:
            TypeError: if any of the arguments aren't of int type.
            ValueError: if any of the arguments are negatives.
        """
        super(Rectangle, self).__init__(id)
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is a getter method for the width private attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This is the setter method for the width private attribute.
        Args:
            value (int): the value that width will be assigned to.
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This is a getter method for the height private attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """This is the setter method for the height private attribute.
        Args:
            value (int): the value that height will be assigned to.
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This is a getter method for the x private attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """This is the setter method for the x private attribute.
        Args:
            value (int): the value that x will be assigned to.
        """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This is a getter method for the y private attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """This is the setter method for the width private attribute.
        Args:
            value (int): the y that width will be assigned to.
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method returns the area of rectangle object.
        """
        return (self.width * self.height)

    def display(self):
        """This method prints in stdout the Rectangle object with the
        character ``#``.
        """
        for vo in range(self.__y):
            print()
        for i in range(self.__height):
            for ho in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the string representation of a rectangle object.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args):
        """This method updates the values of a Rectangle Object's attributes.
        Args:
            args[0] (int): changes the id attribute.
            args[1] (int): changes the width attribute.
            args[2] (int): changes the height attribute.
            args[3] (int): changes the x attribute.
            args[4] (int): changes the y attribute.
        """
        count = 0
        for arg in args:
            if count == 0:
                self.id = arg
            elif count == 1:
                self.__width = arg
            elif count == 2:
                self.__height = arg
            elif count == 3:
                self.__x = arg
            elif count == 4:
                self.__y = arg
            count += 1
