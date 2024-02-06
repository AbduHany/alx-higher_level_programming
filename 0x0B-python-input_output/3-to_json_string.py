#!/usr/bin/python3
"""This module defines the function ``to_json_string``
"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation
    of an object (string)
    Args:
        my_obj (str): The string that will be converted to its
            json representation.
    """
    return (json.dumps(my_obj))
