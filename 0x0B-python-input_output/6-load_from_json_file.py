#!/usr/bin/python3

"""Module - 6-load_from_json_file
Creates an Object from a json file
"""


import json


def load_from_json_file(filename):
    """Creating an Object from json file"""

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
