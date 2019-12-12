#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if (sys.argv[2] == "+"):
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif (sys.argv[2] == "-"):
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif (sys.argv[2] == "*"):
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif (sys.argv[2] == "/"):
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
