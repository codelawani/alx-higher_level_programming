#!/usr/bin/python3
"""Define a write file function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename (any): file to be written to
        text (any): text to be written to file
    Returns:
        The number of characters written"""
    with open(filename, 'w') as f:
        return f.write(text)
