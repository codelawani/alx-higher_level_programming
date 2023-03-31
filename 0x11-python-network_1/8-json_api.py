#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter"""

if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if argv[1:] else ""
    response = requests.post(url, data={'q': q})
    try:
        response = response.json()
        if len(response) == 0:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
