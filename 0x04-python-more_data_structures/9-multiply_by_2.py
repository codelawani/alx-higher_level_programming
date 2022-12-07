#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = a_dictionary.keys()
    values = a_dictionary.values()
    values = list(map(lambda x: x * 2, values))
    new_dict = dict(zip(keys, values))
    return new_dict
