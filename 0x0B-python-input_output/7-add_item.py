#!/usr/bin/python3

"""
a script that adds all arguments to a Python list,
and then save them to a file
"""
import sys

save_json = __import__("5-save_to_json_file.py").save_to_json_file
load_json = __import__("6-load_from_json_file.py").load_from_json_file

filname = "add_item.json"

try:
    json_list = load_json(filename)

except FileNotFoundError:
    json_list = []

for i in argv[1:]:
    json_list.append(i)

save_json(json_list, filename)
