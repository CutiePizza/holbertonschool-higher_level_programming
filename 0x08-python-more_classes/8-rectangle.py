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
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculate the rectangle's area
        Returns: An int
        """
        return self.__width*self.__height

    def perimeter(self):
        """Calculate the rectangle's perimeter
        Returns: An int
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width*2) + (self.__height*2)

    def __str__(self):
        """
        print rectangles
        """
        h = self.__height
        w = self.__width
        if h == 0 or w == 0:
            return ""
        mat = ""
        symbol = self.print_symbol
        for i in range(h):
            for j in range(w):
                mat += " ".join(symbol)
            if i != h - 1:
                mat += " ".join("\n")
        return mat

    def __repr__(self):
        """return a string representation of
        the rectangle to be able to recreate a new instance
        """
        return 'Rectangle({}, {})'.format(self.__width, self.height)

    def __del__(self):
        """prints Bye rectangle...
        when a rectangle is destructed
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area
        of both given rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
