#!/usr/bin/python3
"""
Module with a function add_integer

see doctest for test
"""


def add_integer(a, b=98):
    """
    This function makes the addition of two numbers
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a + b)
