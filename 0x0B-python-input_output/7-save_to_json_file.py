#!/usr/bin/python3
"""
Module for JSON files
"""


def save_to_json_file(my_obj, filename):
    """save a python object to a json file
    Args:
        my_obj: python object
        filename: json file
    """
    import json
    with open(filename, mode='w', encoding='UTF8') as f:
        my_str = json.dumps(my_obj)
        f.write(my_str)
