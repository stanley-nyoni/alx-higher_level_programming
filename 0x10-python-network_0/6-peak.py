#!/usr/bin/python3

"""Find the peak in a list"""


def find_peak(list_of_integers):
    """Find the peak in a list"""
    if list_of_integers is None or list_of_integers == []:
        return None

    lower = 0
    upper = len(list_of_integers) - 1
    while lower < upper:
        mid = (lower + upper) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lower = mid + 1
        else:
            upper = mid
    return list_of_integers[lower]
