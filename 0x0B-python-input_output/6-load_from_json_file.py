#!/usr/bin/python3
"""Define a json file loader"""
import json


def load_from_json_file(filename):
    """ creates object from a JSON text file
    Args:
        filename (any): JSON file to be loaded
    Return:
        created object
    """
    with open(filename, 'r') as f:
        return json.load(f)
