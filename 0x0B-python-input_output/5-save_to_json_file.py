#!/usr/bin/python3

"""
a function that writes an Object to a text file,
using a JSON representation:

"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation:

    Parameters:
        my_obj: json text
        filename: file name
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
