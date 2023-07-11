#!/usr/bin/python3

"""" public instance method """


class BaseGeometry:

    """ public instance methond """
    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")

    """ public instance method that validate value """

    def integer_validator(self, name, value):
        """ raise exception """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
