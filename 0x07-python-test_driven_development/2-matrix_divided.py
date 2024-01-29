#!/usr/bin/python3
"""
This module defines a function (matrix_divided) that divides
all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of matrix and returns
    the divided elements in a new matrix.

    Args:
        matrix (list of lists): The matrix that has a list of
            integers to be divided.
        div (int or float): the number by which the matrix
            elements will be divided.
    Returns:
        a new matrix will all the results which are rounded to 2 places.
    Raises:
        TypeError: if matrix isn't a list of lists of integers or floats.
        TypeError: if the matrix row sizes aren't equal.
        TypeError: if div isn't an int or float.
        ZeroDivisionError: if div is equal to 0.
    """
    if (type(matrix) is not list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for row in matrix:
        if (type(row) is not list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if (len(row) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if (type(element) is not int) and (type(element) is not float):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if (type(div) is not int) and (type(div) is not float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    newmatrix = []
    for row in matrix:
        newrow = []
        for element in row:
            result = element / div
            newrow.append(round(result, 2))
        newmatrix.append(newrow)
    return newmatrix
