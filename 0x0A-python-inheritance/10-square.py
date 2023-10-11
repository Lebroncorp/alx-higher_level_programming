#!/usr/bin/python3
"""
Contains the class Square and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square"""

    def __init__(self, size):
        """An instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns area of the square"""
        return self.__size ** 2
