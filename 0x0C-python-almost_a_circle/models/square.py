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
        """String represantation of a square"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Upadates square using args and kwargs"""

        if args is not None and len(args) != 0:
            if len(args) == 1:
                if isinstance(args[0], int):
                    self.id = args[0]
                else:
                    raise TypeError("id must be an integer")
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if isinstance(value, int):
                        self.id = value
                    else:
                        raise TypeError("id must be an integer")
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
    
    def to_dictionary(self):
        base_dict = super().to_dictionary()

        base_dict["size"] = self.size
        del base_dict["width"]
        del base_dict["height"]

        return base_dict
