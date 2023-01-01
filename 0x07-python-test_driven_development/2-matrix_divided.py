#!/usr/bin/python3


"""
Module containing a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by argument passed to ``div``."""

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    try:
        new = [[round(num / div, 2) for num in row] for row in matrix]
    except TypeError:
        raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
    for i in range(len(matrix)):
        if (len(matrix[i]) != len(matrix[0])):
            raise TypeError('Each row of the matrix must have the same size')
    return new
# return [(list(map(lambda num: round(num / div, 2), row))) for row in matrix]
