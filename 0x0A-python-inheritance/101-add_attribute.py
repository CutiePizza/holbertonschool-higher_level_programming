#!/usr/bin/python3
"""
Functions that adds attribute to an object
"""


def add_attribute(obj, key, value):
    if obj.__dir__:
        return True

