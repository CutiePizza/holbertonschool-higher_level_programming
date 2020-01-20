#!/usr/bin/python3
"""
Module with a function print_square
this module in your file to use the function print_square
Example: See docstring
"""


def text_indentation(text):
    """
    Function that prints My name and last name
    """
    if type(text) is not str or len(text) == 0:
        raise TypeError("text must be a string")
    i = 0
    while i != len(text):
        a = text[i - 1]
        bool1 = a == "?" or a == ":" or a == "."
        bool2 = text[i] == " "
        if bool1 and bool2:
            print(text[i + 1], end="")
            i += 1
        elif text[i] == "?" or text[i] == ":" or text[i] == ".":
            print(text[i])
        else:
            print(text[i], end="")
        i = i + 1
