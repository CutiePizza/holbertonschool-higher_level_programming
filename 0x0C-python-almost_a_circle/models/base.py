#!/usr/bin/python3
"""
Module with class 1
"""


class Base:
    """
    Doctest for class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method of class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        To json dictionary
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))
