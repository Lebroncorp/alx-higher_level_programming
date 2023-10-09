#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """A class with public instance area, integer_validator"""
    def area(self):
        """raises an exception that writes"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value, is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Representation of a rectangle"""
    def __init__(self, width, height):
        """An instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
