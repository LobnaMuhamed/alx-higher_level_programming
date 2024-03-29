#!/usr/bin/python3

"""
a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    a function that multiplies 2 matrices
    """
    if (not isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if (not isinstance(m_b, list)):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    new_mat = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += ((m_a[i][k]) * (m_b[k][j]))
            row.append(sum)
        new_mat.append(row)
    return new_mat
