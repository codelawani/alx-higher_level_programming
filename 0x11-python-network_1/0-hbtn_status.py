#!/usr/bin/python3
"""This script fetches https://intranet.hbtn.io/status
    using the urllib package"""

if __name__ == "__main__":
    from urllib.request import urlopen
    url = 'https://intranet.hbtn.io/status'
    with urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
