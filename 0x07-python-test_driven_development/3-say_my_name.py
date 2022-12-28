#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>.

    Raises:
        TypeError: if first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
