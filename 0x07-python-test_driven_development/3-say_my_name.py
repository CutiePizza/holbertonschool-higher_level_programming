#!/usr/bin/python3
"""
Module with a function say_my_name
Import this module in your file to use the function say_my_name
Example: See docstring
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name and last name
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        if len(last_name) == 0:
            print("My name is {}".format(first_name))
        else:
            print("My name is {} {}".format(first_name, last_name))
    else:
        if not isinstance(first_name, str) or first_name is None:
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
