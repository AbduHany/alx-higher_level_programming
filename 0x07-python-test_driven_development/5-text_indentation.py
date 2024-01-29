#!/usr/bin/python3
""" Module to print text with 2 new lines after `.`, `?` and `:`.
"""


def text_indentation(text):
    """Function to print test with 2 new lines after characters `.`, `?`
        and `:`
    Args:
        text (str): the string to be printed in the specified format.
    Raises:
        TypeError: if text isn't a string.
    """
    if (type(text) is not str):
        raise TypeError("text must be a string")

    newtext = ""
    i = 0

    while (i < len(text)) and (text[i] == ' '):
        i += 1

    while (i < len(text)):
        newtext += text[i]
        if (text[i] == "\n") or (text[i] in ".:?"):
            if (text[i] in ".:?"):
                newtext += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            i += 1
    print(newtext, end="")
