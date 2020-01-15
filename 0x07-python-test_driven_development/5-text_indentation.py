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
    print(text[0], end="")
    for i in range(len(text)):
        if text[i] == "?" or text[i] == ":" or text[i] == ".":
            print("\n")
        else:
            try:
                print(text[i + 1], end="")
            except IndexError:
                pass
