#!/usr/bin/python3

"""10-student - Defines a class Student"""


class Student:
    """Initialising a Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for x in attrs:
                if hasattr(self, x):
                    my_dict[x] = getattr(self, x)
            return my_dict
