#!/usr/bin/python3
"""Module that have a class MyList that inherits from list"""


def is_same_class(obj, a_class):
    """Function that returns True if the object
     is exactly an instance of the specified class"""
    return type(obj) == a_class
