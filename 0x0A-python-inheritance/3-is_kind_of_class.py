#!usr/bin/python3
"""
Function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """return if obj is in aninstnce of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
