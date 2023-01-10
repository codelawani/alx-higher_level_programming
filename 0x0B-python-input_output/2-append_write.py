#!/usr/bin/python3
"""Define a append write file function"""


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8)
    Args:
        filename (any): file to be written to
        text (any): text to be written to file
    Returns:
        The number of characters written"""
    with open(filename, 'a') as f:
        return f.write(text)
