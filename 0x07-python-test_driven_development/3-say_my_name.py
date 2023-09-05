#!/usr/bin/python3

"""
    Module containing  a function to print my name
    Say my name
"""


def say_my_name(first_name, last_name=""):
    """ Prints a string with my name
        Raises exception in case names are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
