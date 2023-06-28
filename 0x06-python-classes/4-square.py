#!/usr/bin/python3
""" Class Square that defines sqaure"""


class Square:
    """ Class Sqaure that defines sqaure"""
    def __init__(self, size=0):
        """
        Initialize Sqaure
        Parameter:
        size: integer
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve sqaure
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        set size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """
        calculate area of sqaure
        """
        return self.__size**2
