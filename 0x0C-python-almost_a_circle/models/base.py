#!/usr/bin/python3

"""
The First Class Base:
    attributes:
        __nb_objects
    initialize class method
"""


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
            id = Base.__nb_objects
