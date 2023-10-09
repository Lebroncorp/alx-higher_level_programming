#!/usr/bin/python3
"""
this module contains function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance  is an instance of, or if the object is an
    instance of a class that inherited from a_class, else False"""
    return (isinstance(obj, a_class))
