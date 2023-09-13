#!/usr/bin/python3

"""Module - 7-add_item
Adds all arguments to the python list and then to the file
"""


import json
import sys
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = 'add_item.json'
arg_list = list()

if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
    arg_list = load_from_json_file(file_name)

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        arg_list.append(arg)

save_to_json_file(arg_list, file_name)
