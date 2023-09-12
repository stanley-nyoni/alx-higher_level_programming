#!/usr/bin/python3

""""Reads a text file"""


def read_file(filename=""):
    """"Reading  from a txt file"""
    
    with open(filename, "r", encoding="utf-8") as f:
        read_chars = f.read()
        while (len(read_chars) > 0):
            print(read_chars, end="")
            read_chars = f.read()
        print()
