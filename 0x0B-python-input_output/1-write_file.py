#!/usr/bin/python3
"""This module defines the function ``write_file``.
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file and
    returns the number of characters written.
    Args:
        filename (str): the name of the file to be created.
        text (str): the text that will be written to the file.
    """
    with open(filename, mode="w", encoding='utf-8') as f:
        return f.write(text)
