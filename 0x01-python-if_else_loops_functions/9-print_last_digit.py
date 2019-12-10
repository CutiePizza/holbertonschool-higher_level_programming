#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = -10
    else:
        n = 10
    print("{:d}".format(abs(number % n)), end="")
    return (abs(number % n))
