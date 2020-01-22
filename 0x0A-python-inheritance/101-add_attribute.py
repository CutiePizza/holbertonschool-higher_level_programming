#!/usr/bin/python3
"""
Functions that adds attribute to an object
"""


def add_attribute(obj, key, value):
    my_tuple = (float, int, str, bool)
    if isinstance(obj, my_tuple):
        obj.key = value
    else:
        raise TypeError("can't add new attribute")
