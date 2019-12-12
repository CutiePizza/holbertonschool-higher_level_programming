#!/usr/bin/python3
import sys
s = 0
if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print("0")
    else:
        for i in range(1, len(sys.argv)):
            s += int(sys.argv[i])
        print(s)
