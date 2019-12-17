#!/usr/bin/python3
def no_c(my_string):
    for char in 'C|c':
        my_string = my_string.replace(char, '')
    return (my_string)
