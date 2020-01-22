#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """Class Student
    Attributes:
        first_name: first name
        last_name: last name
        age: age
    """
    def __init__(self, first_name, last_name, age):
        """Initilize attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict
        """
        a_dict = {}
        if attrs is not None:
            for i in range(len(attrs)):
                if attrs[i] in self.__dict__:
                    a_dict[attrs[i]] = self.__dict__[attrs[i]]
            return a_dict
        return self.__dict__
