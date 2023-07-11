#!/usr/bin/python3

""" Class MyInt """



class MyInt(int):
    """ class Myint """

    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
