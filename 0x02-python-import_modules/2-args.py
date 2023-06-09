#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_arg = len(sys.argv) - 1
    if len_arg == 0:
        print("0 arguments.")
    elif len_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len_arg))
    for i in range(len_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
