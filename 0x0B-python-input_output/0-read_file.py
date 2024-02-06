#!/usr/bin/python3
"""This module defines function ``read_file``
"""


def read_file(filename=""):
    """This function reads a text file and prints it
    to stdout.
    Args:
        filename (str): the name of the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        filetext = f.read()
        print(filetext, end="")
