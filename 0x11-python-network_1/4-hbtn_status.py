#!/usr/bin/python3
"""This script fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
