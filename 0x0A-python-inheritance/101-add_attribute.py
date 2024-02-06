#!/usr/bin/python3
"""This module defines a function that adds attribute to an object.
"""


def add_attribute(obj, name, value):
    """Function that adds an attribute to object if it can.
    Args:
        obj: object to where the new attribute will be added
        name: name of the attribute that'll be added.
        value: value of the new attribute that'll be added.
    """
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
