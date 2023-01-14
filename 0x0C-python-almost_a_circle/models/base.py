#!/usr/bin/python3
import json
"""base"""


class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises base class"""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps([dictionary for dictionary in list_dictionaries])
        else:
            return '"[]"'

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance
