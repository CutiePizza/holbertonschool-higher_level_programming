#!/usr/bin/python3
"""
Module for class t json
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    of an object
    """
    a = obj.__dict__
    return (a)
