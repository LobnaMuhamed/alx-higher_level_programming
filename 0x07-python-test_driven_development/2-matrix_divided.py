#!/usr/bin/python3

"""
a function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix"""
    len_row = len(matrix[0])
    new_mat = []
    str_err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0 or div == float('inf'):
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        if len(row) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if ((not isinstance(i, int)) and (not isinstance(i, float))):
                raise TypeError(str_err)
            new_value = round(i / div, 2)
            new_row.append(new_value)
        new_mat.append(new_row)
    return new_mat
