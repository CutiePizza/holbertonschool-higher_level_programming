#!/usr/bin/python3
"""
Print a pascal triangle
"""


def pascal_triangle(n):
    if n is None:
        return None
    if n <= 0:
        return ([])
    mat = []
    val = 1
    for i in range(n):
        mini = []
        for j in range(i + 1):
            if j is 0:
                val = 1
            else:
                val = val * (i - j + 1)//j
            mini.append(val)
        mat.append(mini)
    return (mat)
