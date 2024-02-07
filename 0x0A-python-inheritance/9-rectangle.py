#!/usr/bin/python3
"""Module of BaseGeometry Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Method that initializes the instance"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method that returns the string representation of the instance"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
