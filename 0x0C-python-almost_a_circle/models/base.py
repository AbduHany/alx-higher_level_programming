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

    @classmethod
    def save_to_file(cls, list_objs):
        """This class method writes the JSON string representation
        of list_objs to a file.
        Args:
            list_objs (list): list of objects that inherit from Base class.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding='utf-8') as f:
            if (list_objs is None):
                f.write("[]")
            else:
                dictionary_list = []
                for element in list_objs:
                    dictionary_list.append(element.to_dictionary())
                f.write(cls.to_json_string(dictionary_list))
