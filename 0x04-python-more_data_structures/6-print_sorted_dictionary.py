#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = dict(sorted(a_dictionary.items()))
    for k, v in zip(new.keys(), new.values()):
        print("{:s}: {}".format(k, v))
