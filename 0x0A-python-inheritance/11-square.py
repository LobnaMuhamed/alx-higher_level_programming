#!/usr/bin/python3

""" a class Square that inherits from Rectangle (9-rectangle.py) """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        """ initialize square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """ represent square """
        return (f"[Square] {self.__size}/{self.__size}")
