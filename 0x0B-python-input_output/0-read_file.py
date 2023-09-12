#!/usr/bin/python3

""""Reads a text file"""


def read_file(filename=""):
    """"Reading  from a txt file
    Args:
        filename:str : name of file
    """
    with open(filename, "r") as f:
        read_chars = f.read()
        while (len(read_chars) > 0):
            print(read_chars)
            read_chars = f.read()
