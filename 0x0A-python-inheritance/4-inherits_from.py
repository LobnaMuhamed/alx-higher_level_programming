#!/usr/bin/python3

""" a function that returns True if object is instance of a class """


def inherits_from(obj, a_class):
    """ a function that returns True if object is instance of a class """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
