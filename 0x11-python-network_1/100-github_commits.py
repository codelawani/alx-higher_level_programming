#!/usr/bin/python3
"""This script prints the 10 most recent commits on the
    master branch of the repository “rails” by the user "rails"""

if __name__ == '__main__':
    from requests import get
    from sys import argv
    REPO = argv[1]
    OWNER = argv[2]
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/commits'
    resp = get(url)

    for i in range(10):
        try:
            NAME = resp.json()[i].get('commit').get('author').get('name')
            SHA = resp.json()[i].get('sha')
            print(f'{SHA}: {NAME}')
        except (AttributeError, IndexError):
            break
