#!/usr/bin/python3
def uniq_add(my_list=[]):
    cp_list = my_list.copy()
    new_list = []
    sum = 0
    for i in cp_list:
        count = 0
        for j in my_list:
            if j == i:
                count += 1
            if count == 2:
                continue
        if count == 1:
            new_list.append(j)
            sum += j
    return (sum)
