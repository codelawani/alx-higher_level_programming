#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Creates a rectangle with height and width attributes"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialise Rectangle object"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def area(self):
        """gets area of rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """gets perimeter of rectangle object"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """creates a new string object from given object"""
        rect = ''
        for col in range(self.__height):
            for row in range(self.__width):
                rect += type(self).print_symbol
            if col != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """Return the canonical string representation of the object"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints message when object is about to be destroyed"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

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
