#!/usr/bin/python3
"""This module defines the class ``MyInt``.
"""


class MyInt(int):
    """This class defines a rebel class ``MyInt``
    that acts as a rebel to its parent ``int`` and
    has 2 methods.
    """
    def __eq__(self, value):
        """This method returns false if MyInt and other value are equal.
        Args:
            value (int): value that MyInt object will be compared to.
        """
        return not int.__eq__(self, value)

    def __ne__(self, value):
        """This method returns True if MyInt and other value are equal.
        Args:
            value (int): value that MyInt object will be compared to.
        """
        return not int.__ne__(self, value)
