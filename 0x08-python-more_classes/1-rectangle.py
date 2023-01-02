#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Creates a rectangle with height and width attributes"""

    def __init__(self, width=0, height=0):
        """Initialise Rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of Rectangle object"""
        return self._width

    @width.setter
    def width(self, width):
        """Sets width of Rectangle object"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self._width = width

    @property
    def height(self):
        """Retrieves height of current object"""
        return self._height

    @height.setter
    def height(self, height):
        """Sets height of current object"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self._height = height
