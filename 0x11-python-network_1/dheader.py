#!/usr/bin/python3

from sys import argv
from requests import get

if __name__ == '__main__':
    with get(argv[1]) as r:
        print(r.headers['X-Request-Id'])
