#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    max_num = my_list[0]
    if len_list == 0:
        return None
    for i in range(len_list - 1):
        if max_num > my_list[i]:
            continue
        else:
            max_num = my_list[i]
    return max_num
