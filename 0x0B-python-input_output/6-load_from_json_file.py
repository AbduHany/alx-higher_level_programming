#!/usr/bin/python3
"""This module defines the function ``load_from_json_file``.
"""
import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file.
    Args:
        filename (str): the file that contains the JSON string to
            be converted to a python Object.
    """
    with open(filename, encoding='utf-8') as f:
        pythonobj = json.load(f)
        return pythonobj
