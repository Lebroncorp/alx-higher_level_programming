#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """reversed version of operators"""

    def __new__(cls, *args, **kwargs):
        """create new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """inverts != to now =="""
        return int(self) != other

    def __ne__(self, other):
        """inverts == to now !="""
        return int(self) == other
