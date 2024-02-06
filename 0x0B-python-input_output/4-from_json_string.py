#!/usr/bin/python3
"""This module defines the function ``from_json_string``.
"""
import json


def from_json_string(my_str):
    """This function returns an object
    (Python data structure) represented by a JSON string.
    Args:
        my_str (str): the json str that will be converted
            to python object.
    """
    return (json.loads(my_str))
