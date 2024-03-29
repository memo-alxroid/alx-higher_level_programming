#!/usr/bin/python3

"""Module for Rectangle class."""


class Rectangle:
    """This is the class Rectangle."""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The __init__ method of the class."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """The getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """The getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """The area method of the class."""
        return self.__width * self.__height

    def perimeter(self):
        """The perimeter method of the class."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """The __str__ method of the class."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """The __repr__ method of the class."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """The __del__ method of the class."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
