#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    a function that replaces an element of a list at a specific position
    ...
    Parameters
    ----------
    my_list: list
        The list of integers
    idex: int
        The given index
    element: new element that will be replaced

    Return:
    if idx < 0 or idx > len of list, return original list
    else, return new list

    """
    len_list = len(my_list) - 1

    if idx < 0 or idx > len_list:
        return None
    else:
        my_list[idx] = element
        return(my_list)
