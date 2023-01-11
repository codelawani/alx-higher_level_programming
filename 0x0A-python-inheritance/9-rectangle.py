#!/usr/bin/python3
"""Defines a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Gets rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description"""
        return f'[Rectangle] {self.__width}/{self.__height}'
