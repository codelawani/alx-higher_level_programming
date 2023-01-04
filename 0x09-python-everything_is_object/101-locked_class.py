#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """Locked class that only allows assignment of first name"""

    __slots__ = ['first_name']

    def __init__(self, value=None):
        self.first_name = value
