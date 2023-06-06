#!/usr/bin/python3
import string
for char in string.ascii_lowercase:
    if char != "q" and char != "e":
        print("{}".format(char), end='')
    else:
        continue
