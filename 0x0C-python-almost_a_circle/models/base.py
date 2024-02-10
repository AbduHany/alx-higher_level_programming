#!/usr/bin/python3
"""This module defines a class named ``Base``.
"""
import json


class Base:
    """This class defines a base for all models.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This method initializes a Base object/instance with an id.
        Args:
            id (int): represents an id for the object, if not given (==None)
                then the class attribute ``__nb_objects`` is incremented and
                and its value is assigned to the object's id.
        """
        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return ("[]")
        return (json.dumps(list_dictionaries))
