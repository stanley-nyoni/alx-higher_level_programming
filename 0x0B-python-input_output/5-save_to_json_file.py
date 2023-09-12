#!/usr/bin/python3

"""Module - 5-save_to_json_file
Writes an object to a file in json
"""


import json


def save_to_json_file(my_obj, filename):
    """Writing Object to a text file
    Args:
        my_obj: object passed
        filename: str: name of file to be written
    """
    j_s = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(j_s)
