#!/usr/bin/python3
"""
Find peak
"""

def find_peak(list_of_integers):
    """
    method to find peak
    """
    if len(list_of_integers) == 0:
        return (None)
    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        try:
            if (list_of_integers[i] > list_of_integers[i + 1] and
                    list_of_integers[i] > list_of_integers[i - 1]
                    ):
                    peak = list_of_integers[i]
        except IndexError:
            pass
    return (peak)
