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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            with open(filename, mode='w', encoding='UTF-8') as f:
                l = []
                f.write(l)
        else:
            l = []
            with open(filename, mode='w', encoding='UTF-8') as f:
                for i in list_objs:
                    l.append(i.to_dictionary())
                f.write(cls.to_json_string(l))
