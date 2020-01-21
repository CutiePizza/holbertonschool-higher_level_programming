#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Class Square
"""


class Square(Rectangle):
    """Defines a Square
    """

    def __init__(self, size):
        """Square's constructor
        Args:
            square (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate the Square's area
        Returns: An int
        """
        return self.__size**2

    def __str__(self):
        """print something
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
