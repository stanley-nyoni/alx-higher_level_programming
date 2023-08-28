#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:    
        res = my_function(1, 4)
    except NameError:
        raise NameError(message)

