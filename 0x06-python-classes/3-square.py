#!/usr/bin/python3

"""
class Square that defines a square
"""


class Square:

    """ class Square that defines a square"""

    def __init__(self, size=0):
        """
        initializing Square
        parameters:
            size: integer (sqaure's size)
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """
        area of square
        Return:
            area
        """
        return self.__size**2