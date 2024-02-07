#!/usr/bin/python3
"""Module of BaseGeometry Class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class that inherits from Rectangle"""
    def __init__(self, size):
        """Method that initializes the instance"""
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method that returns the area of the square"""
        return self.__size ** 2
