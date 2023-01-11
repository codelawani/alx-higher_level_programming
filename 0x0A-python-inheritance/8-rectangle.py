#!/usr/bin/python3
"""Defines a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Assigns width and height attributes"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
        super().integer_validator('height', height)
