#!/usr/bin/python3

"""
    Module that prints square
    Square to be represented by #
    print_square
"""


def print_square(size):
    """ Prints the square of size
        Raises exception, in case size is not int, size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
