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

    def to_json(self):
        """ returns a dictionary representaion """
        return self.__dict__
