#!/usr/bin/python3
"""This module contains a rebel int subclass """


class MyInt(int):
    """Rebel int subclass with == and != inverted"""

    def __init__(self, value):
        """Initialise class"""
        self.value = value

    def __eq__(self, x):
        """"overload '==' operator"""
        return self.value != x

    def __ne__(self, x):
        """ooverload '!=' operator"""
        return self.value == x
