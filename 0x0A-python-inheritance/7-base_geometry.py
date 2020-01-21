#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """Defines a Geometry base for future classes
    """

    def area(self):
        """Method area that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a value
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
