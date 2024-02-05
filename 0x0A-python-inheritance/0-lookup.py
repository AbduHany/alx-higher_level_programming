#!/usr/bin/python3
""" This module defines the function ``lookup``
"""


def lookup(obj):
    """This function returns a list of all attributes
    attached to an object.
    """
    return dir(obj)
