#!/usr/bin/python3
"""Module defines a function that multiplies 2 matrices.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices together
    Args:
        m_a (list): first list of lists containing ints to be multiplied
        m_b (list): second list of lists contining ints to be multiplied
    Returns:
        product matrix
    """
    productmatrix = numpy.matmul(m_a, m_b)
    return productmatrix
