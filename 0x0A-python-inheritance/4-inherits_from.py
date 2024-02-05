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
    if issubclass(obj.__class__, a_class.__bases__):
        return True
    else:
        return False
