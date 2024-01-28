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
    for i in range(len(text)):
        if text[i] in ".:?":
            newtext += text[i]
            newtext += "\n\n"
            continue
        elif text[i] == ' ' and (text[i - 1] in ".:?"):
            continue
        newtext += text[i]
    print(newtext, end="")
