#!/usr/bin/python3
"""This module defines a class that's locked
to only contain the attribute ``first_name``
"""
class LockedClass(object):
    """This class is a locked class that could
    only hold an attribute named ``first_name``
    """
    __slots__ = ['first_name']
