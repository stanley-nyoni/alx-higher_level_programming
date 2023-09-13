#!/usr/bin/python3

"""8-class_to_json
Returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """Returning the simple data structure
    Args:
        obj: object
    """

    return obj.__dict__
