#!/usr/bin/python3

"""Add attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """Adding new attribute to obj
    Args:
        obj: object
        attr_name: attribute name
        attr_value: attribute value
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
