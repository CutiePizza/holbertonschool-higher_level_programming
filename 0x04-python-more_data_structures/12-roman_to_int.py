#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    rv = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
    val = 0
    for i in range(len(roman_string)):
        if roman_string[i] in rv:
                if rv[roman_string[i]] > rv[roman_string[i - 1]]:
                    val += (rv[roman_string[i]] - 2 * rv[roman_string[i - 1]])
                else:
                    val += rv[roman_string[i]]
        else:
            return 0
    return val
