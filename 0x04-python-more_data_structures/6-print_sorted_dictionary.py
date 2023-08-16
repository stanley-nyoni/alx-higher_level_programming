#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_d = sorted(a_dictionary)
    for i in s_d:
        print("{:s}: {}".format(i, a_dictionary[i])) 
