#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class that inherits from a rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialise square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square object"""
        return (
            f"[{self.__class__.__name__}] \
({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update class attributes"""
        argc = len(args)
        if args:
            self.id = args[0]
            if argc > 1:
                self.size = args[1]
            if argc > 2:
                self.x = args[2]
            if argc > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
