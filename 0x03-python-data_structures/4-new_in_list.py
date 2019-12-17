#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ret = []
    for i in range(0, len(my_list)):
        ret.append(my_list[i])
    ret[idx] = element
    return (ret)
