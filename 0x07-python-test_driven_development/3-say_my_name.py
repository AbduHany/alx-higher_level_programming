#!/usr/bin/python3
"""This module defines a function (say_my_name) that prints a name."""


def say_my_name(first_name, last_name=""):
    """
    Prints my name is <first name> <last name>
    Args:
        first_name (str): The first name string.
        last_name (str): The last name string, treated
            as an empty string by default if not given.

    Returns: None.
    Raises:
        TypeError: if first_name or last_name aren't of
            type string.
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
