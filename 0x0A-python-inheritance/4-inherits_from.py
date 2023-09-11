#!/usr/bin/python3

"""Inherits from"""


def inherits_from(obj, a_class):
    """ Return true if obj inherits from a_class"""

    obj_type = type(obj)
    return isinstance(obj, a_class) and obj_type != a_class
