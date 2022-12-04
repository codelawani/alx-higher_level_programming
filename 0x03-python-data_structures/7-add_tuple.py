#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
#    if len(tuple_b) == 2:
    if not tuple_b[1]:
        b = 0
    if not tuple_a[1]:
        a = 0
    x = tuple_a[0]
    y = tuple_b[0]
    a = tuple_a[1]
    b = tuple_b[1]
    print(f"b:{b}")
    new = (x + y, a + b)
    return new
