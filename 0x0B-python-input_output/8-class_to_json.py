#!/usr/bin/python3
"""This module defines the function ``class_to_json``.
"""
import json


def class_to_json(obj):
    """This function returns the dictionary description with
    simple data structure for JSON serialization of an object.
    Args:
        obj (class instance): the class whose attributes will be
            serialized.
    """
    return (obj.__dict__)
