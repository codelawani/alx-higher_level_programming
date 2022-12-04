#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
    if la >= 2:
        a0, a1 = tuple_a[0], tuple_a[1]
    if lb >= 2:
        b0, b1 = tuple_b[0], tuple_b[1]
    if la == 1:
        a0, a1 = tuple_a[0], 0
    if lb == 1:
        b0, b1 = tuple_b[0], 0
    if la == 0:
        a0, a1 = 0, 0
    if lb == 0:
        b0, b1 = 0, 0
    new_t = (a0 + b0, a1 + b1)
    return new_t
