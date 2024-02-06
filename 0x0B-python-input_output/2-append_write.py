#!/usr/bin/python3
"""This module defines the function ``append_write``.
"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text
    file and returns the number of characters added.
    Args:
        filename (str): the name of the file to be created.
        text (str): the text that will be written to the file.
    """
    with open(filename, mode="a", encoding='utf-8') as f:
        return f.write(text)
