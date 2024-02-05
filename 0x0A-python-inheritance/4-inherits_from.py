#!/usr/bin/python3
"""This module defines the function ``inherits_from``
"""


def inherits_from(obj, a_class):
    if issubclass(obj.__class__, a_class.__bases__):
        return True
    else:
        return False
