#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ok = set()
    ok = set(set_1 ^ set_2)
    return (ok)
