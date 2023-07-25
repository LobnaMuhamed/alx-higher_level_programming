#!/usr/bin/python3

"""
The First Class Base:
"""
import json
import csv


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

    """ a class method returns instance with all attributes already set """
    @classmethod
    def create(cls, **dictionary):
        """ a class method returns instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)

    """ a class method that returns a list of instances """
    @classmethod
    def load_from_file(cls):
        """ a class method that returns a list of instances """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []
        data = cls.from_json_string(json_string)
        instances_list = []
        for instance_data in data:
            instance = cls.create(**instance_data)
            instances_list.append(instance)
        return (instances_list)

    """ a class method that serializes an deserialize in CSV """
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ a class method that write the JSON string """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
            else:
                _list = []
                for obj in list_objs:
                    _list.append(obj.to_dictionary())
                f.write(Base.to_json_string(_list))

    """ a class method that serializes an deserialize in CSV """
    @classmethod
    def load_from_file_csv(cls):
        """ a class method that returns a list of instances """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, encoding="utf-8") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []
        data = cls.from_json_string(json_string)
        instances_list = []
        for instance_data in data:
            instance = cls.create(**instance_data)
            instances_list.append(instance)
        return (instances_list)
