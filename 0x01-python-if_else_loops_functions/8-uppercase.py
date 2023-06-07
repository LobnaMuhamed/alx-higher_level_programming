#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        if ord(i) in range(ord('a'), ord('z')+1):
            i = chr(ord(i) - 32)
            new_str += i
        else:
            new_str += i
    print("{}".format(new_str), end='')
    print()
