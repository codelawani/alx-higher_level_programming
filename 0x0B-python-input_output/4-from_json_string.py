#!/usr/bin/python3
"""Define a json_string converter"""
import json


def from_json_string(my_str):
    """ converts json_string to object(Python data structure)
    Args:
        my_str (any): the string
    Returns:
        object(Python data structure)"""
    return json.loads(my_str)
