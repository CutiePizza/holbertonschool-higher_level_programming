#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Defines a Rectangle by it's height and width
    Attributes:
        height (int): Height of the rectangle
        width (int): Width of the rectangle
    """

    @property
    def width(self):
        """Retrieve rectangle's width
        Returns:
        int: Recangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the Rectangl's width value
        Args:
        value (int): Rectangle's width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve rectangle's height
        Returns:
        int: Recangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the Rectangl's height value
        Args:
        value (int): Rectangle's height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """Rectangle's constructor
        Args:
            width (int): default value 0
            height (int): default value 0
        """
        self.height = height
        self.width = width
