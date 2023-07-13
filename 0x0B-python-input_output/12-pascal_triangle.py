#!/usr/bin/python3

"""
function that resturns a list of integers representing
Pascal's traingle of n

"""


def pascal_triangle(n):
    matrix = []
    if n <= 0:
        return ([])
    else:
        for i in range(1, n + 1):
            row = []
            for j in range(1, i + 1):
                if j == 1 or j == i:
                    row.append(1)
                else:
                    x = matrix[i - 2][j - 2] + matrix[i - 2][j - 1]
                    row.append(x)
            matrix.append(row)
    return matrix
