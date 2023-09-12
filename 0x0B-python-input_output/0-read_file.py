#!/usr/bin/python3

""""Reads a text file"""


def read_file(filename=""):
    """"Reading  from a txt file
    Args:
        filename:str : name of file
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
        print()
