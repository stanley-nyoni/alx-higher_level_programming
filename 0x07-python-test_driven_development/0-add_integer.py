#!/usr/bin/python3
"""
    Module that contains a function
    to calculate the sum of 2 integers
    Returns the sum
"""


def add_integer(a, b=98):
    """Computes and returns the sum of a and b
        Raise exception, if a or b are not integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif isinstance(a, float):
        a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(b, float):
        b = int(b)

    return a + b
