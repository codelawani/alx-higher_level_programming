#!/usr/bin/python3
def no_c(my_string):
    new_s = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_s += ch
    return new_s
