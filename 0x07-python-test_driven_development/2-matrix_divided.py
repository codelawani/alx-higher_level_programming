#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be an integer')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    try:
        new = [[round(num / div, 2) for num in row] for row in matrix]
    except TypeError as e:
        print('matrix must be a matrix (list of lists) of integers/floats')
    else:
        return new
# return [(list(map(lambda num: round(num / div, 2), row))) for row in matrix]
