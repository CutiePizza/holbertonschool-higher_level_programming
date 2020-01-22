#!/usr/bin/python3
"""
Module for files
"""


def read_file(filename=""):
    """Function that reads a given file
    and prints its lines
    Args:
        filename: given file
    """
    with open(filename, mode='r', encoding='UTF8') as f:
        for line in f:
            print(line, end="")
