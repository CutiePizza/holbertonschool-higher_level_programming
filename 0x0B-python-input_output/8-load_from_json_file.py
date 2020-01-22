#!/usr/bin/python3
"""
Module for JSON files
"""


def load_from_json_file(filename):
    """save a python object to a json file
    Args:
        filename: json file
    """
    import json
    with open(filename, mode='r', encoding='UTF8') as f:
        r = f.read()
        return (json.loads(r))
