#!/usr/bin/python3
"""This module contains a pascal_triangle generator"""


def pascal_triangle(n):
    """Generates pascal triangle of size n"""

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    matrix = [[1], [1, 1]]
    for k in range(1, n - 1):
        temp = [1, 1]
        j = 1
        for i in range(1, len(matrix[k])):
            temp.insert(j, matrix[k][i] + matrix[k][i - 1])
            j += 1

        matrix.append(temp)
    return matrix
