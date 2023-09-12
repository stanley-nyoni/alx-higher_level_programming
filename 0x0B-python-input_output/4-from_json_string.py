#!/usr/bin/python3

"""Module - 4-from_json_string
    Returns an object represented by JSON.
"""


import json


def from_json_string(my_str):
    """Returning an object from json
    Args:
        my_str: str: string
    """
    return json.loads(my_str)
