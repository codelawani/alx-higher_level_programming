#!/usr/bin/python3
from sys import argv
from urllib import request, parse

url = argv[1]
data = {'email': argv[2]}
data = parse.urlencode(data).encode('utf-8')
with request.urlopen(url, data) as r:
    response = request.urlopen(r)
    print(response)
