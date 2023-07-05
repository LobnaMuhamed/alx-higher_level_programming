#!/usr/bin/python3
""" define class Rectangle """


class Rectangle:

    """ A class variable, counting number of instance"""
    number_of_instances = 0

    """ A public class attribute for print symbol """
    print_symbol = '#'

    """ Intialize Rectangle class """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    """ get_width function"""

    @property
    def width(self):
        return self.__width

    """ set width function """

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ get height function """

    @property
    def height(self):
        return self.__height

    """ set height function """

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """ calculate area of rectangle """

    def area(self):
        return self.__width * self.__height
    """ calculate perimeter of rectangle """

    def perimeter(self):
        if (self.__width) == 0 or (self.__height == 0):
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
    """ print rectangle with # """

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        result = ''
        for i in range(self.__height):
            if i == (self.__height - 1):
                result += str(self.print_symbol) * self.__width
            else:
                result += str(self.print_symbol) * self.__width + '\n'
        return result
    """ function return a string representation of rectangle """

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    """ function that print message when instance is deleted """

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
