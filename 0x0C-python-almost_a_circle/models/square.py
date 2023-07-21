#!/usr/bin/python3

""" class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):

    """ class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize class Square with size attribute
        """
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ create __str__ method """
        return(f"[Square] {self.id} {self.x}/{self.y} - {self.size}")
