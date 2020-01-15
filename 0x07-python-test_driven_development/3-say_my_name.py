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
    if type(first_name) is str and type(last_name) is str:
        if len(last_name) == 0:
            print("My name is {} ".format(first_name))
        else:
            print("My name is {} {}".format(first_name, last_name))
    else:
        if type(first_name) is not str or first_name is None:
            raise TypeError("first_name must be a string")
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")
