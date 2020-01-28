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
        msg = '[Square] ({}) {}/{} - {}/{}'
        return msg.format(self.id, self.x, self.y, self.width, self.height)
