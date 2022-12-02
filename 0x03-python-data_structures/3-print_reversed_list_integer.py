#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list) - 1
    for i in range(count, -1, -1):
        print(my_list[i])
