#!/usr/bin/python3
"""
Subclass of list
"""


class MyList(list):
    """
    Subclass of list
    """

    def print_sorted(self):
        """print list sorted
        """
        print(sorted(self))

    def __str__(self):
        """return list
        """
        return str(list(self))
