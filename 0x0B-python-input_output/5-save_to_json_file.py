#!/usr/bin/python3
"""Define a json file saver"""
import json


def save_to_json_file(my_obj, filename):
    """ writes object to text file using
    JSON representation
    Args:
        my_obj (any): the object
        filename (any): file to be written to
    Returns:
        nothing"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
