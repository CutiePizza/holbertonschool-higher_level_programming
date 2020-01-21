#!/usr/bin/python3
"""
Functions that adds attribute to an object
"""


def add_attribute(obj, key, value):
    if not hasattr(obj, key):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
