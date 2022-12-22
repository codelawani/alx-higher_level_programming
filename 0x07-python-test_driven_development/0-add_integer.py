#!/usr/bin/python3
def add_integer(a, b=98):
    """ Returns integer addition of a and b.

    Float arguments are typecasted as integers before addition

    Raises:
        TypeError: if either a or b are non-integer or non-float.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and  not isinstance(b, float):
        raise TypeError('b must be an integer')
    return(int(a) + int(b))
