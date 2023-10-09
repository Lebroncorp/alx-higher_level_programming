#!/usr/bin/python3
"""
This module contains function is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is exactly an instance a_class, otherwise false"""
    return (type(obj) == a_class)
