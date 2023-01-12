#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialises a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__


""" class Student:
"""     """Defines a student"""
"""
       def __init__(self, first_name, last_name, age):
   """         """Initialises a student"""
"""        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
"""         """retrieves a dictionary representation of a Student instance"""
"""        result = self.__dict__
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            values = []
            for key in attrs:
                if key not in self.__dict__.keys():
                    continue
                values.append(self.__dict__[key])
            result = dict(zip(attrs, values))
        return result """
