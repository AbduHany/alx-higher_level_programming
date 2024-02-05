#!/usr/bin/python3
"""This module defines the function ``is_same_class``
"""


def is_same_class(obj, a_class):
    """function returns True if obj is exactly an instance of
    ``a_class``
    Args:
        obj (object): the object we're testing
        a_class (class): class we're testing
    """
    if (type(obj) is a_class):
            return True
    else:
        return False
