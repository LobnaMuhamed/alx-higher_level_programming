#!/usr/bin/python3

"""
a function that inserts a line of text to a file,
after each line containing a specific string

"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string

    """

    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        if len(lines) == 1 and search_string in lines[0]:
            lines.append(new_string)
        else:
            for index, line in enumerate(lines):
                if search_string in line:
                    lines.insert(index + 1, new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
