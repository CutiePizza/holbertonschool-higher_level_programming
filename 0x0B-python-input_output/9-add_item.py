#!/usr/bin/python3
import json
import os
load = __import__('8-load_from_json_file').load_from_json_file
save = __import__('7-save_to_json_file').save_to_json_file

"""
Script to add arguments to json file
"""

filename = "add_item.json"
if len(sys.argv) == 1:
    item = []
    save(item, filename)
else:
    my_obj = load(filename)
    for i in range(1, len(sys.argv)):
        my_obj.append(sys.argv[i])
    save(my_obj, filename)
