#!/usr/bin/python3

"""
a function that prints a text with 2 new lines after each
of these characters: ., ?, :
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each
    of these characters: ., ?, :
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    beginning_of_line = True
    for i in text:
        if (i == "." or i == "?" or i == ":"):
            print(i, end="")
            print("\n")
            beginning_of_line = True
        elif i == " " and beginning_of_line:
            pass
        else:
            print(i, end="")
            beginning_of_line = False
