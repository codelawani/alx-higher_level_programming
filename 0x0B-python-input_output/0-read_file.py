#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        print(f.read().strip())
