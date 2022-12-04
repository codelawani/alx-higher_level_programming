#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element != row[0]:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print("")
