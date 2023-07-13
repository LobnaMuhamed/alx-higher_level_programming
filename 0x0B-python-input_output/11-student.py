#!/usr/bin/python3

"""
a class Student that defines a student
"""


class Student:
    """
    intialize class

    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns a dictionary representation

        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        that replaces all attributes of the Student instance
        """
        for key in json:
            setattr(self, key, json[key])
