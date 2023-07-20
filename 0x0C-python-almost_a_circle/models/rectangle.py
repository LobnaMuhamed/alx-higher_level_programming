#!/usr/bin/python3

"""
Class Rectangle that inherits from Base:
"""
from models.base import Base


class Rectangle(Base):
    """
    Inialize Class Rectangle with:
        Parameters:
            width, height, x, y, id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """ get width function """
    @property
    def width(self):
        """ get width function """
        return self.__width

    """ set width function """

    @width.setter
    def width(self, value):
        """ set width function """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ get height function """

    @property
    def height(self):
        """ get height function """
        return self.__height

    """ set height function """

    @height.setter
    def height(self, value):
        """ set height function """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ get x function """

    @property
    def x(self):
        """ get x function """
        return self.__x

    """ set x function """
    @x.setter
    def x(self, value):
        """ set x function """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ get y function """
    @property
    def y(self):
        """ get y function """
        return self.__y

    """ set y function """

    @y.setter
    def y(self, value):
        """ set y function """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value
