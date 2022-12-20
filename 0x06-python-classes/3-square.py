#!/usr/bin/python3
"""Defines a square """


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize square class
        Args: size - size of defined square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """computes area of current square
        Returns:
            The current square area
        """
        return self.__size ** 2
