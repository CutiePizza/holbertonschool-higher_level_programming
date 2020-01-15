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
        if text[i] == "?" or text[i] == ":" or text[i] == ".":
            print(text[i])
            print("")
        else:
            if (text[i - 1] == "?" or text[i - 1] == ":" or text[i - 1] == ".")
            and
            (text[i] == " "):
                print(text[i + 1], end="")
                i += 1
            else:
                print(text[i], end="")
        i = i + 1
