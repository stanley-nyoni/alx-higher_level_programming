#!/usr/bin/python3

"""100-append_after"""


def append_after(filename='', search_string='', new_string=''):
    """Searches and replaces string
    Args:
        filename: name of file
        search_string: string to be search for
        new_string: string to be appended
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
