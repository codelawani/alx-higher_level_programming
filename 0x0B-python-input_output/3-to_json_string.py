#!/usr/bin/python3
"""Define a json_string converter"""
import json


def to_json_string(my_obj):
    """ Gets the JSON representation of an object (string)
    Args:
        my_obj (any): the object
    Returns:
        the JSON representation of an object (string)"""
    return json.dumps(my_obj)
