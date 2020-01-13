#!/usr/bin/python3
"""
Module with a function add_integer
Import this module in your file to use the function add_integer
Example: See docstring
"""


def add_integer(a, b=98):
    """
    This function makes the addition of two numbers
    """
    numeric = (int, float)
    if not isinstance(a, numeric):
        raise TypeError("a must be an integer")
    if not isinstance(b, numeric):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
