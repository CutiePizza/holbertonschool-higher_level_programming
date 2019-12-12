#!/usr/bin/python3
import sys
if __name__ == "__main__":
    path = dir(sys.path.append('./hidden_4.pyc'))
    for i in range(0, len(path)):
        if path[i][0] != '_':
            print(path[i], end="\n")
