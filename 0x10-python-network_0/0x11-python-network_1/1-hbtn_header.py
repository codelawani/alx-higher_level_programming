#!/usr/bin/python3
"""This script fetches a header from https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print(response.getheader('X-Request-Id'))
