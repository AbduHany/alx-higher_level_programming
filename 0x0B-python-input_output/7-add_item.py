#!/usr/bin/python3
"""This module contains a script that adds all arguments to
a python list and then save them to a file.
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if (os.path.exists('add_item.json')):
    pylist = load_from_json_file('add_item.json')
else:
    pylist = []
for i in range(1, len(sys.argv)):
    pylist.append(sys.argv[i])
save_to_json_file(pylist, 'add_item.json')
