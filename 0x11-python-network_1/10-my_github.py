#!/usr/bin/python3
"""This script takes your Github credentials (username and password) and
    uses the Github API to display your id"""
from sys import argv
import requests
if __name__ == "__main__":
    response = requests.get(
        'https://api.github.com/user', auth=(argv[1], argv[2]))
    print(response.json().get('id'))
