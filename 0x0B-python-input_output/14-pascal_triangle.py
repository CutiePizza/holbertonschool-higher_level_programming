#!/usr/bin/python3
"""
Print a pascal triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return ([])
    mat = [[1]]
    val = 1
    for i in range(1, n):
        mini = []
        for j in range(i + 1):
            if j is 0:
                val = 1
            else:
                val = val * (i - j + 1)/j
            mini.append(int(val))
        mat.append(mini)
    return (mat)
