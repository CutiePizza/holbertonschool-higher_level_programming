#!/usr/bin/python3
"""
Module for files
"""


def append_write(filename="", text=""):
    """Append text to a given file (otherwise creates it)
    and returns number of character added
    Args:
        filename: the file, can be an empty string
        text: Number of lines to read from filename
    """
    with open(filename, mode='a', encoding='UTF8') as f:
        w = f.write(text)
    return w
