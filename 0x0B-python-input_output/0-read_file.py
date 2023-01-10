#!/usr/bin/python3
"""Defines a function that prints file content"""


def read_file(filename=""):
    """Prints read file contents to stdout
    Args:
        filename (str): file to be read"""
    with open(filename) as f:
        print(f.read().strip())
