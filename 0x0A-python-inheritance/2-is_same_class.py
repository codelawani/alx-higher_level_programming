#!/usr/bin/python3
"""This module checks if an object is an
exact instance of a class"""


def is_same_class(obj, a_class):
    """This function returns True if an object is an exact instance of a class
    otherwise, it returns False"""
    return type(obj) is a_class
