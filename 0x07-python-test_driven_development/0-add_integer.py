#!/usr/bin/python3

""" a function that adds 2 integers """


def add_integer(a, b=98):
    """ a function that adds 2 integers """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return int(result)
