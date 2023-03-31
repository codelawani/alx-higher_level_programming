#!/usr/bin/python3
"""This script fetches a header from https://intranet.hbtn.io/status"""
from sys import argv
from requests import get

if __name__ == "__main__":
    response = get(argv[1])
    print(response.headers.get('X-Request-Id'))
