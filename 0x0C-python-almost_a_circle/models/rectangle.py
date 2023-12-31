#!/usr/bin/python3

"""Define a Rectangle Class that inherits from Base class"""

from models.base import Base


class Rectangle(Base):
    """Initializes a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Retrieves the x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x value"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Retrieves the y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y value"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Computes and returns the area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """Print the represantation of rectangle to stdout"""
        for y in range(self.y):
            print()

        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string represantion of a rectangle object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle attributes using arbitrary args"""

        if args is not None and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.width = args[1]
            elif len(args) == 3:
                self.height = args[2]
            elif len(args) == 4:
                self.x = args[3]
            elif len(args) == 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the Rectangle dictionary represantion"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
