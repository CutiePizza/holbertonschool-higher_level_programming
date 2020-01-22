#!/usr/bin/python3
"""
Module for files
"""


def number_of_lines(filename=""):
    """Returns number of lines of a file
    Args:
        filename: given file
    """
    with open(filename, mode='r', encoding='UTF8') as f:
        n = sum(1 for line in f)
    return n
