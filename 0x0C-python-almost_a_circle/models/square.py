#!/usr/bin/python3

"""Defines a Square class that inherits from a Rectangle class
    Square - a special rectangle
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initializing a Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

        self.size = size

    @property
    def size(self):
        """Retrieves square size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the square size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.size)
