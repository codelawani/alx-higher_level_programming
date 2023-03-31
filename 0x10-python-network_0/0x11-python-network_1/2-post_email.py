#!/usr/bin/python3
"""This script sends a POST request to the passed URL
    with the email as a parameter,
    and displays the body of the response (decoded in utf-8)"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
