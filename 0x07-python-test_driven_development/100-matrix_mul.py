#!/usr/bin/python3
"""Module defines a function that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices together
    Args:
        m_a (list): first list of lists containing ints to be multiplied
        m_b (list): second list of lists contining ints to be multiplied
    Returns:
        product matrix
    Raises:
        TypeError: if m_a or m_b aren't lists or
            if m_a or m_b aren't lists of lists or
            if m_a or m_b lists don't have ints or floats or
            if m_a or m_b aren't rectangles (same row sizes).
        ValueError: if m_a or m_b are empty or
            if m_a and m_b can't be multiplied.
    """
    if (type(m_a) is not list):
        raise TypeError("m_a must be a list")
    if (type(m_b) is not list):
        raise TypeError("m_b must be a list")

    if (m_a == []) or (m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == []) or (m_b == [[]]):
        raise ValueError("m_b can't be empty")

    a_row_count = len(m_a)
    b_row_count = len(m_b)
    a_column_count = len(m_a[0])
    b_column_count = len(m_b[0])
    for row in m_a:
        if (type(row) is not list):
            raise TypeError("m_a must be a list of lists")
        for element in row:
            if (type(element) is not int) and (type(element) is not float):
                raise TypeError("m_a should contain only integers or floats")
        if (len(row) != a_column_count):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if (type(row) is not list):
            raise TypeError("m_b must be a list of lists")
        for element in row:
            if (type(element) is not int) and (type(element) is not float):
                raise TypeError("m_a should contain only integers or floats")
        if (len(row) != b_column_count):
            raise TypeError("each row of m_b must be of the same size")

    if (a_column_count != b_row_count):
        raise ValueError("m_a and m_b can't be multiplied")
    productmatrix = []
    for i in range(len(m_a)):
        newrow = []
        for j in range(b_column_count):
            sum = 0
            for k in range(b_row_count):
                sum += (m_a[i][k] * m_b[k][j])
            newrow.append(sum)
        productmatrix.append(newrow)
    return productmatrix
