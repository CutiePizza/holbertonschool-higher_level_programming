#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Class Rectangle
"""


class Rectangle(BaseGeometry):
    """Defines a Rectangle
    """

    def __init__(self, width, height):
        """Rectangle's constructor
        Args:
            width (int): default value 0
            height (int): default value 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the rectangle's area
        Returns: An int
        """
        return self.__width*self.__height

    def __str__(self):
        """print something
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
