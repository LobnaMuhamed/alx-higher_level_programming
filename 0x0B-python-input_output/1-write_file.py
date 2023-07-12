#!/usr/bin/python3

""" writing a string to a text file (UTF8) and returns the number """


def write_file(filename="", text=""):
    """ writing a string to a text file (UTF8) and returns the number """

    with open(filename, "w", encoding="utf-8") as f:
        nb_characters = f.write(text)
    return (nb_characters)
