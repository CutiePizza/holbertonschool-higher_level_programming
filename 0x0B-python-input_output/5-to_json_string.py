#!/usr/bin/python3
"""
Module for objects
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj (any): object
    """
    import json
    return json.dumps(my_obj)
