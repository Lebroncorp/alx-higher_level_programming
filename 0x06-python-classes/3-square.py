#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """represent a square ofprivate instance attribute size"""

    def __init__(self, size=0):
        """initialize function of new square"""

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ returns the area of a given square"""
        return self.__size ** 2
