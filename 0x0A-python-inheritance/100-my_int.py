#!/usr/bin/python3
"""This module defines the class ``MyInt``.
"""


class MyInt(int):


    def __eq__(self, value):
            return not int.__eq__(self, value)
    def __ne__(self, value):
            return not int.__ne__(self, value)
