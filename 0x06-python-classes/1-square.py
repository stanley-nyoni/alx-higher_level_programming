#!/usr/bin/python3

""" Creates a square with size. """


class Square:
    """ Defines a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """ Initialize a square. """
        self.__size = size
