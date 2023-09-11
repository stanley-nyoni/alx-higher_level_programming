#!/usr/bin/python3

"""" Is an instance"""


def is_same_class(obj, a_class):
    """" Returns true if obj is an instance of a class"""

    obj_type = type(obj)
    if obj_type != a_class:
        return False

    return True
