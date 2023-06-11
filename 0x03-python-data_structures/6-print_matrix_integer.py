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
            if i == len(row) - 1:
                print("{:d}".format(row[i]))
            else:
                print("{:d}".format(row[i]), end=" ")
