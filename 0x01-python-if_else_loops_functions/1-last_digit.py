#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = -10
else:
    n = 10
msg1 = "Last digit of {} is {} and is greater than 5"
msg2 = "Last digit of {} is {} and is 0"
msg3 = "Last digit of {} is {} and is less than 6 and not 0"
if number % n > 5:
    print(msg1.format(number, number % n))
elif number % n == 0:
    print(msg2.format(number, number % n))
elif number < 6:
    print(msg3.format(number, number % n))
