#!/usr/bin/python3
"""This script fetches https://intranet.hbtn.io/status"""

from urllib import request
if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
