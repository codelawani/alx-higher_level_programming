#!/usr/bin/python3
"""Define a append write file function"""
import json


def to_json_string(my_obj):
    """ Gets the JSON representation of an object (string)
    Args:
        my_obj (any): the object
    Returns:
        the JSON representation of an object (string)"""
    return json.dumps(my_obj)
