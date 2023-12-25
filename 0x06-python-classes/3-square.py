#!/usr/bin/python3

"""Defines a Square."""


class Square:
    """Square class with private size attribute."""

    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
