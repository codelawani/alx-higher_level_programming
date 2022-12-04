#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        n = 0
        for element in row:
            if n > 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
            n = 1
        print("")
