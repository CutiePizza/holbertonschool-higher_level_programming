#!/usr/bin/python3
"""
Module for objects
"""


def from_json_string(my_str):
    """Returns the Object representation of a JSON string
    Args:
        my_str (string): JSON string
    """
    import json
    return json.loads(my_str)
