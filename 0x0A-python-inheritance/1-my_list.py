#!/usr/bin/python3

""""My List """


class MyList(list):
    """""Defines my list class"""
    def print_sorted(self):
        print(sorted(self))
