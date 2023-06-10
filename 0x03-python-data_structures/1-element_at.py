#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list like in C
    ...

    Parameters
    ----------
    my_list : list optional
        The list of integers
    idx: int
        The given index
    Return:
        if idx is negative, return None
        if idx is out of range, return None
        else => return element when found
    """
    len_list = len(my_list)

    if idx < 0 or idx > len_list:
        return None
    else:
        return (my_list[idx])
