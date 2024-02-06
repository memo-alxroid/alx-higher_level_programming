#!/usr/bin/python3
"""Module of BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class that has a method area()
     that raises an Exception"""
    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        return value
