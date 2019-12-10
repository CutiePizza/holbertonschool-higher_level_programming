#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = -10
else:
    n = 10

if number % n > 5:
    print("Last digit of {} is {} and is greater than 5"
            .format(number, number % n))
elif number % n == 0:
    print("Last digit of {} is {} and is 0"
            .format(number, number % n))
elif number < 6:
    print("Last digit of {} is {} and is less than 6 and not 0"
            .format(number, number % n))
