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
    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method that returns the JSON string of list_dictionaries """
        if not list_dictionaries or list_dictionaries is []:
            return ("[]")
        return json.dumps(list_dictionaries)

    """ a class method that write the JSON string """
    @classmethod
    def save_to_file(cls, list_objs):
        """ a class method that write the JSON string """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
            else:
                _list = []
                for obj in list_objs:
                    _list.append(obj.to_dictionary())
                f.write(Base.to_json_string(_list))

    """ a static method that returns the list of the JSON string """
    @staticmethod
    def from_json_string(json_string):
        """ a static method that returns the list of the JSON string """
        if not json_string or json_string is []:
            return([])
        return json.loads(json_string)
