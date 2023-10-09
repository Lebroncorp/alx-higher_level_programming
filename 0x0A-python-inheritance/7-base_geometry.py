#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with area and integer_validator"""
    def area(self):
        """raises an exception that writes"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value, an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
