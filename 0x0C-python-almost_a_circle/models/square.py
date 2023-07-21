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
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    """ get size function """

    @property
    def size(self):
        """ get size function """
        return self.width

    """ set size function """

    @size.setter
    def size(self, value):
        """ set size function """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    """ a public method that assigns attributes """
    def update(self, *args, **kwargs):
        """ a public method that assigns attributes """
        attr_names = ["id", "size", "x", "y"]
        if not args and kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
