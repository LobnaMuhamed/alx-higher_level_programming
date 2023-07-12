#!/usr/bin/python3

""" appending a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):

    """ appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Parameters:
        filename: file name
        text: text will be appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        nb_char_added = f.write(text)
    return (nb_char_added)
