#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 96 and ord(char) <= 128:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{:s}".format(result))
