#!/usr/bin/python3
"""
Module for files
"""


def write_file(filename="", text=""):
    """Writes to a given file (otherwise creates it)
    and returns number of character written
    Args:
        filename: the file, can be an empty string
        text: Number of lines to read from filename
    """
    with open(filename, mode='w', encoding='UTF8') as f:
        w = f.write(text)
    return w
