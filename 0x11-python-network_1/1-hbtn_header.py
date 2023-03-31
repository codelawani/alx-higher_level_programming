#!/usr/bin/python3
"""This script fetches a header from https://intranet.hbtn.io/status"""

from urllib import request
from sys import argv
if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
