#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays the
    body of the response"""


if __name__ == "__main__":
    from sys import argv
    import requests
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
