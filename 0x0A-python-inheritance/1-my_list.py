#!/usr/bin/python3
"""This module inherits from built in list"""


class MyList(list):
    """class that inherits from built in list"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
