#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    a function that prints a matrix of integers
    ......
    parameters
    ==========
    matrix: a input matrix of integers
    """
    for row in matrix:
        for i in range(len(row)):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(row[i]), end="")
        print()
