#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_arg = len(sys.argv) - 1
    result = 0
    for i in range(len_arg):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
