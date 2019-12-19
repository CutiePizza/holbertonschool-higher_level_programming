#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for j in range(len(matrix)):
        mini = []
        for k in range(len(matrix[j])):
            mini.append(matrix[j][k] ** 2)
        new.append(mini)
    return (new)
