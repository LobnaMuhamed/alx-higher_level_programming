#!/usr/bin/python3

""" a function that reads a text file (UTF8) """


def read_file(filename=""):

    """ a function that reads a text file (UTF8)

        Args:
            filename (str): the file name
    """

    with open(filename, encoding="utf-8") as f:
        for i in f:
            print(i, end="")
