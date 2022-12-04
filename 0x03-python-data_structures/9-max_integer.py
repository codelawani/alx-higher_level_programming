#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    return sorted(my_list)[len(my_list) - 1]
