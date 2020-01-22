#!/usr/bin/python3
"""
Function inherits_from
"""


def inherits_from(obj, a_class):
    """returns if an obj inherits from a_class
    or not
    """
    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
