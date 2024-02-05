#!/usr/bin/python3
"""This module defines the function ``inherits_from``
"""


def inherits_from(obj, a_class):
    """This function returns True if ``obj`` is inherited from
    ``a_class``
    Args:
        obj (object): the objects that's being tested.
        a_class (class object): the class that we're testing against.
    """
    parents = obj.__class__.__bases__
    for parent in parents:
        if issubclass(parent, a_class):
            return True
    return False
