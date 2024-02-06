#!/usr/bin/python3
"""This module defines the class ``Student``.
"""


class Student:
    """This class represents a Student object.
    """
    def __init__(self, first_name, last_name, age):
        """This method initiates the Student class instance
        with the values (first_name, last_name, age)
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The student's age in years.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method retrieves a dictionary representation of a
        student instance
        """
        return (self.__dict__)
