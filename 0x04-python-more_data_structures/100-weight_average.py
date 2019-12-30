#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mul = 0
    su = 0
    for i in range(len(my_list)):
        mul += my_list[i][0] * my_list[i][1]
        su += my_list[i][1]
    return mul / su
