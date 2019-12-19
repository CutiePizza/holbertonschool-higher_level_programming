#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    roman_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
    val = 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman_val:
            val += roman_val[roman_string[i]]
        else:
            return 0
    return val
