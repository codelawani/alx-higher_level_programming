#!/usr/bin/python3
"""This module contains a rebel int subclass """


class MyInt(int):
    """Rebel int subclass with == and != inverted"""

    def __init__(self, value):
        """Initialise class"""
        self.num = value

    def __eq__(self, x):
            """"overload '==' operator"""
        if self.num == x:
            return False
        return True

    def __ne__(self, x):
        """ooverload '!=' operator"""
        if self.num != x:
            return False
        return True
