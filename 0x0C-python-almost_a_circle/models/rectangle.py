#!/usr/bin/python3
"""rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value of width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """gets value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value of height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """gets value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets value of x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """gets value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets value of y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Gets Rectangle area"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(''.join([' ' * self.x] +
                  ['#' * self.width]))

    def __str__(self):
        """Prints Rectangle object"""
        return (
            f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """update class attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args):
            i = 0
            for arg in args:
                setattr(self, attributes[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
