#!/usr/bin/python3
"""
Contains inherits_from function
"""


def inherits_from(obj, a_class):
    """returns True if obj is instance/inherited from a_class, else false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
