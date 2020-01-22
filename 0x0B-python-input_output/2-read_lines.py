#!/usr/bin/python3
"""
Module for files
"""


def read_lines(filename="", nb_lines=0):
    """Returns number of lines of a given file
    Args:
        filename: the file
        nb_lines: Number of lines to read from filename
    """
    with open(filename, mode='r', encoding='UTF8') as f:
        if nb_lines is 0:
            for line in f:
                print(line, end='')
        else:
            for i in range(nb_lines):
                print(f.readline(), end='')
