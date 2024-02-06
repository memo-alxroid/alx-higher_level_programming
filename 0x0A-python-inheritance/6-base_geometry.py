#!/usr/bin/python3
"""Module of BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class that has a method area()
     that raises an Exception"""
    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")
