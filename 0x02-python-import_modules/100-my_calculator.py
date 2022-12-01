#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    ac = len(sys.argv) - 1
    av = sys.argv
    if ac != 3:
        print(f"Usage: {av[0]:s} <a> <operator> <b>")
        exit(1)
    op = av[2]
    a = int(av[1])
    b = int(av[3])
    if op == '+':
        print(f"{a:d} + {b:d} = {add(a,b):d}")
    elif op == '-':
        print(f"{a:d} - {b:d} = {sub(a,b):d}")
    elif op == '*':
        print(f"{a:d} * {b:d} = {mul(a,b):d}")
    elif op == '/':
        print(f"{a:d} / {b:d} = {div(a,b):d}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
