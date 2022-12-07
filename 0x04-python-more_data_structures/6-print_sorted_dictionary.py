#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = dict(sorted(a_dictionary.items()))
    keys = new.keys()
    values = new.values()
    for k, v in zip(keys, values):
        print("{:s}: {}".format(k, v))
