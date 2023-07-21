#!/usr/bin/python3

"""
The First Class Base:
"""
import json


class Base:
    """
    The First Class Base:
        attributes:
            __nb_objects
        initialize class method
    """

    __nb_objects = 0

    """ Initialze method of Class """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    """ static method that returns the JSON string of list_dictionaries """
    def to_json_string(list_dictionaries):
        """ static method that returns the JSON string of list_dictionaries """
        if list_dictionaries is None or list_dictionaries is []:
            return ("[]")
        return json.dumps(list_dictionaries)
