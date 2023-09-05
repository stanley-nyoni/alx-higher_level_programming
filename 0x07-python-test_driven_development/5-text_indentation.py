#!/usr/bin/python3

"""
    Text Indentation
    This moduele prints a text with 2 new lines after each of these
    characters . ? :
"""


def text_indentation(text):
    """
        Prints text with 2 new lines after some chars
        Raises exception in case text is not string """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in text:
        if character in [".", "?", ":"]:
            print(character, end="\n\n")
        else:
            print(character, end="")
