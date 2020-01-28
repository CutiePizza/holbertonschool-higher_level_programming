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
        l = []
        if list_objs is None:
            with open(filename, mode='w', encoding='UTF-8') as f:
                f.write(cls.to_json_string(l))
        else:
            with open(filename, mode='w', encoding='UTF-8') as f:
                for i in list_objs:
                    l.append(i.to_dictionary())
                f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        import json
        l = []
        if json_string is None:
            return l
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        r = cls(1, 1, 1, 1)
        r.update(**dictionary)
        return r
