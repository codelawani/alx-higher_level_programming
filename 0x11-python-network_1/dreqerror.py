#!/usr/bin/python3
from sys import argv
import requests as rq

res = rq.get(argv[1])
if res.status_code >= 400:
    print(f'Error code: {res.status_code}')
