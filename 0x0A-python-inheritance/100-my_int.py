#!/usr/bin/python3
"""
Class MyInt
"""


class MyInt(int):
    """A rebel subclass of MyInt
    """

    def __ne__(self, value):
        """
        """
        if isinstance(value, int):
            return value == value
        return False

    def __eq__(self, value):
        """return true if not equal
        """
        return not self.__ne__(value)
