#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    path = dir(hidden_4)
    for i in range(0, len(path)):
        if path[i][0] != '_':
            print(path[i], end="\n")
