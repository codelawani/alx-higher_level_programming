#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Creates a rectangle with height and width attributes"""

    def __init__(self, width=0, height=0):
        """Initialise Rectangle object"""
        self.width = width
        self.height = height

    def area(self):
        """gets area of rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """gets perimeter of rectangle object"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        rect = ''
        for row in range(self.__height):
            for row in range(self.__width):
                rect += '#'
            rect +='\n'
        return rect

    @property
    def width(self):
        """Retrieves width of Rectangle object"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width of Rectangle object"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Retrieves height of current object"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height of current object"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
