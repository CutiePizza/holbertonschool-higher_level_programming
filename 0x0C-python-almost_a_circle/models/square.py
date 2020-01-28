#!/usr/bin/python3
"""
Module for Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Init method
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str method
        """
        msg = '[Square] ({}) {}/{} - {}'
        return msg.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update method"""
        if args is not None and len(args) != 0:
            if len(args) >= 1 and len(args) != 0:
                self.id = args[0]
            if len(args) >= 2 and len(args) != 0:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3 and len(args) != 0:
                self.x = args[2]
            if len(args) >= 4 and len(args) != 0:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k) is True:
                    setattr(self, k, v)
