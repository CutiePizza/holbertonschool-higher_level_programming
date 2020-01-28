#!/usr/bin/python3
from models.base import Base
"""
Module for rectangle
"""


class Rectangle(Base):
    """
    Claas Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        return width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        sets width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        return height
        """
        return(self.__height)

    @height.setter
    def height(self, height):
        """
        sets height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        return x
        """
        return(self.__x)

    @x.setter
    def x(self, x):
        """
        sets x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        returns y
        """
        return(self.__y)

    @y.setter
    def y(self, y):
        """
        sets y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate the rectangle's area
        Returns: An int
        """
        return self.width*self.height

    def display(self):
        """
        display
        """
        h = self.height
        w = self.width
        string = "#" * w
        s = string
        for i in range(1, h):
            s += "\n" + string
        print(s)

    def __str__(self):
        """
        str method
        """
        msg = '[Rectangle] ({}) {}/{} - {}/{}'
        return msg.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """
        update method
        """
        if len(args) >= 1 and len(args) != 0:
            self.id = args[0]
        if len(args) >= 2 and len(args) != 0:
            self.width = args[1]
        if len(args) >= 3 and len(args) != 0:
            self.height = args[2]
        if len(args) >= 4 and len(args) != 0:
            self.x = args[3]
        if len(args) >= 5 and len(args) != 0:
            self.y = args[4]
