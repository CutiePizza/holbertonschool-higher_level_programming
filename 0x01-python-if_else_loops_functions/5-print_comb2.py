#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        print(i, end="")
        if j == 9 and i == 9:
            print(j)
        else:
            print(j, end=", ")
