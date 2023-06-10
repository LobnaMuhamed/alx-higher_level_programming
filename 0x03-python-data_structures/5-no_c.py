#!/usr/bin/python3
def no_c(my_string):
    """
    a function that removes all characters c and C from a string
    ....
    parameters
    ----------
    my_string: input string
    Return: new string
    """
    new_string = ''
    for i in my_string:
        if i not in ('c', 'C'):
            new_string += i
    return new_string
