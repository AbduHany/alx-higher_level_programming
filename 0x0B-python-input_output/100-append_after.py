#!/usr/bin/python3
"""This module defines the function ``append_after``.
"""


def append_after(filename="", search_string="", new_string=""):
    """This function inserts a line of text to a file, after each line
    containing a specific string.
    Args:
        filename (str): name of file to be appended to.
        search_string (str): string to be searched.
        new_string (str): string to be appended after searched string.
    """
    with open(filename, "r", encoding='utf-8') as f:
        filetext = ""
        for line in f:
            filetext += line
            if search_string in line:
                filetext += new_string
    with open(filename, "w", encoding='utf-8') as f:
        f.write(filetext)
