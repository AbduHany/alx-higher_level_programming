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
        """This method returns the JSON string representation
        of ``list_dictionaries``
        Args:
            list_dictionaries (list): list of dictionaries.
        """
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

    @staticmethod
    def from_json_string(json_string):
        """This static method returns a list of dictionaries from
        the JSON string representation ``json_string``.
        Args:
            json_string (str): A JSON string representation for
                a list of dictionaries.
        """
        if (json_string is None) or (json_string == ""):
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if (cls.__name__ == "Rectangle"):
            newobj = cls(1, 1)
            if "size" in dictionary:
                dictionary["width"] = dictionary["size"]
                dictionary["height"] = dictionary["size"]
            newobj.update(**dictionary)
        elif (cls.__name__ == "Square"):
            newobj = cls(1)
            if "width" in dictionary:
                dictionary['size'] = dictionary['width']
            newobj.update(**dictionary)
        return (newobj)

    @classmethod
    def load_from_file(cls):
        """This method returns a list of instances read
        from a file.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding='utf-8') as f:
                instance_list = []
                content = f.read()
                objects = cls.from_json_string(content)
                for object in objects:
                    newobj = cls.create(**object)
                    instance_list.append(newobj)
                return (instance_list)
        except FileNotFoundError:
            return ([])
