#!/usr/bin/python3
"""This module"""


def add_attribute(obj, attr, value):
    """add attribute to object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
