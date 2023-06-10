#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    replaces an element in a list without modifying the original list
    .....
    Parameters:
    my_list: list
        The list of elements
    idx: int
        The given index
    element: the given element
    """
    len_list = len(my_list) - 1
    new_list = my_list.copy()

    if idx < 0 or idx > len_list:
        return my_list
    else:
        new_list[idx] = element
    return new_list
