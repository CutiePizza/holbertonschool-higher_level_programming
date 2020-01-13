#!/usr/bin/python3
"""
Module with a function matrix_divided
Import this module in your file to use the function matrix_divided
Example: See docstring n tests folder
"""


def matrix_divided(matrix, div):
    """
        Function that divides a mtrix by div
    """
    mat = []
    numeric = (int, float)
    message = "matrix must be a matrix (list of lists) of integers/float"
    if not isinstance(div, numeric):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None:
        raise TypeError(message)
    if (len(matrix) == 0):
        raise TypeError(message)
    for i in range(len(matrix)):
        mini = []
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], numeric):
                mini.append(round(matrix[i][j] / div, 2))
            else:
                raise TypeError(message)
        if (len(mini) == 0):
            raise TypeError(message)
        if j != len(matrix):
            raise TypeError("Each row of the matrix must have the same size")
        mat.append(mini)
    return mat
