#!/usr/bin/python3

"""Defines a Base Class"""


import json


class Base:
    """Initialize a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string format of a list of dicts"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        list_type = type(list_dictionaries)
        if list_type != list or not \
                all(isinstance(x, dict) for x in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json string format to json file"""

        if list_objs is None or list_objs == []:
            json_data = "[]"
        else:
            json_data = \
                cls.to_json_string([x.to_dictionary() for x in list_objs])

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_data)
