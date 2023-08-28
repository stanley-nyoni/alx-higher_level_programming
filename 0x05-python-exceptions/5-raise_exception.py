#!/usr/bin/python3

def raise_exception():
    a = 23
    b = "77"
    try:
        a + b
    except TypeError:
        raise TypeError("")
