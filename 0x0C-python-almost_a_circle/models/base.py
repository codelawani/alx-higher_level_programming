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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps([dictionary for dictionary in list_dictionaries])
        else:
            return '"[]"'

    @classmethod
    def save_to_file(cls, list_objs):
        """returns JSON string representation of list_dictionaries"""
        filename = f"{cls.__name__}.json"
        if list_objs:
            list_of_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(list_of_dicts)
            with open(filename, 'w') as f:
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """converts to python object(list) from JSON string"""
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename) as f:
                list_of_dicts = cls.from_json_string(f.read())
        except (FileNotFoundError):
            return []
        instances_list = [cls.create(**d) for d in list_of_dicts]
        return instances_list
