#!/usr/bin/python3
"""Defines a square """


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize square class
        Args: size - size of defined square
        """
        self.__size = size

    def area(self):
        """computes area of current square
        Returns:
            The current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves size of current square
        Args:
            size (int): The first parameter
        Returns:
            The current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the current size of the square
        Args:
            size (int): The first parameter
            value (int): The second parameter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
