#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main':
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
    print(dir(r))
