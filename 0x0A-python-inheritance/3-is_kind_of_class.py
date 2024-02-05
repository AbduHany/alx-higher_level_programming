#!/usr/bin/python3
"""This module defines the function ``is_kind_of_class``
"""


def is_kind_of_class(obj, a_class):
    """This function returns True if obj is instance of a_class
    Args:
        obj: The object we're testing.
        a_class: the class we're comparing it to.
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
