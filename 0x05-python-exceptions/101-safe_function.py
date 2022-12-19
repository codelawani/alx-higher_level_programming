#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error:
        print('Exception: {}'.format(error), file=stderr)
    finally:
        return None
