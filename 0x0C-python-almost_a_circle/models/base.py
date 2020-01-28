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
        """
        comments
        """
        import json
        l = []
        if json_string is None:
            return l
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method to create a copy of instance
        """
        if cls.__name__ == "Rectangle":
            r = cls(1, 2)
        else:
            r = cls(2)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """
        load from file
        """
        import json
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as f:
                line = f.read()
                line_str = cls.from_json_string(line)
                l = []
                for i in line_str:
                    l.append(cls.create(**i))
                return l
        except:
            return []
