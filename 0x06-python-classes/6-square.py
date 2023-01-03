#!/usr/bin/python3
"""Defines a square """


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize square class
        Args: size - size of defined square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not all(isinstance(x, int) for x in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with character #"""
        for y in range(self.__position[1]):
            print()
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(' ', end='')
            for i in range(self.__size):
                print('#', end='')
            print()
