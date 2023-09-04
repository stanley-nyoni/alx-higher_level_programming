#!/usr/bin/python3
""" Defines a rectangle class."""


class Rectangle:
    """ Initializes a rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiate a rectangle object

        Args:
            width: width of rect
            height: height of rect
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the width of a rect"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of a rect

        Args:
            value: width to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height

        Args:
            value: height to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
