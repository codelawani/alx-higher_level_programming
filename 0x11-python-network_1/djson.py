#!/usr/bin/python3
"""This script"""

from requests import post
url = 'http://0.0.0.0:5000/search_user'
q = argv[1] if argv[1] else ""
query = {'q': q}
resp = post(url, data=query)
try:
    jsonresp = r.json()
    if not jsonresp:
        print('No result')
    else:
        print(f'[{jsonresp.keys}] {jsonresp.get("id")}')
except (JSONDecodeError):
    print('Not a valid JSON')

