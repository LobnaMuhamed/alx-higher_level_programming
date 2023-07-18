#!/usr/bin/pthon3
"""
a function that multiplies 2 matrices by using the module NumPy

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    A function that multiplies 2 matrics using Numpy
    """
    return np.matmul(m_a, m_b)
