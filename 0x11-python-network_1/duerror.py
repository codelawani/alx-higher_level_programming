#!/usr/bin/python3
"""This script"""

from urllib import request, error
from sys import argv

try:
    r = request.urlopen(argv[1])
except error.HTTPError as e:
    print(f'Error code: {e.code}')
else:
    print(r.read())
