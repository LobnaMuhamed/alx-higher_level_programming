#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    a function that prints all integers of a list, in reverse order.
    ....
    Parameters:
    my_list: list => The list of integers
    Return:
       return New reverse List
    """
    len_list = len(my_list) - 1
    for i in range(len_list, -1, -1):
        print("{:d}".format(my_list[i]))
