#!/usr/bin/python3

"""
Write a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    {"is_active": true, 12 }

    Parameters:
        filename: file name
    """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
