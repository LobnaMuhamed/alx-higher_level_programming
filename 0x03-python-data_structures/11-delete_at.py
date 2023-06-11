#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    a function that delete item at specific position
    ---------
    parameter
    =========
    my_list: entry list
    idx: input index
    """
    len_list = len(my_list)
    if idx < 0 or idx > len_list:
        return (my_list)
    for i in range(len_list):
        if i == idx:
            del my_list[i]
    return (my_list)
