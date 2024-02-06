#!/usr/bin/python3
"""This module defines the function ``save_to_json_file``.
"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file, using a JSON
    representation.
    Args:
        my_obj: python data structure that will converted to JSON
            representations
        filename: the name of the file where the JSON representations
            will  be written to.
    """
    with open(filename, "w", encoding='utf-8') as f:
        jsonstr = json.dumps(my_obj)
        f.write(jsonstr)
