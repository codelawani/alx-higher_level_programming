#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except Exception as error:
        result = None
        print(f'Exception: {error}', file=stderr)
    finally:
        return result
