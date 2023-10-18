#!/usr/bin/python3
"""
    Defines a Base class module
"""


class Base:
    """ Base for all other class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the base class with its attributes id(int) """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
