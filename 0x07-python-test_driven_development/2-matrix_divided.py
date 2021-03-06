#!/usr/bin/python3
"""
Module with a function matrix_divided
this module in your file to use the function matrix_divided
Example: See docstring n tests folder
"""


def matrix_divided(matrix, div):
    """
        Function that divides a mtrix by div
    """
    mat = []
    numeric = (int, float)
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None:
        raise TypeError(message)
    if (len(matrix) == 0):
        raise TypeError(message)
    len0 = len(matrix[0])
    for i in range(len(matrix)):
        mini = []
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], numeric):
                n = matrix[i][j] / div
                mini.append(round(n, 2))
            else:
                raise TypeError(message)
        if (len(mini) == 0):
            raise TypeError(message)
        if (len(mini) != len0):
            raise TypeError("Each row of the matrix must have the same size")
        mat.append(mini)
    return mat
