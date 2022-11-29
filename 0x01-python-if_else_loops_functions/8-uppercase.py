#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            c = ord(c) + 32
        print("{:c}".format(c), end='')
