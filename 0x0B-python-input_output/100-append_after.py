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
        textlist = f.readlines()
    with open(filename, "w", encoding='utf-8') as f:
        for i in range(len(textlist)):
            if "Python" in textlist[i]:
                textlist.insert(i + 1, new_string)
        f.writelines(textlist)
