#!/usr/bin/python3
"""This module defines a new subclass MyList
from the class list.
"""


class MyList(list):
    """This subclass is based off the class ``list``
    and it inherits all its fields and methods and adds
    a new method ``print_sorted`` that prints the list sorted.
    """
    def __init__(self):
        """This method initializes a MyList object based on its
        parent's __init__ method.
        """
        super().__init__()

    def print_sorted(self):
        """This method prints a copy of the list object, but sorted.
        """
        print(sorted(self))
