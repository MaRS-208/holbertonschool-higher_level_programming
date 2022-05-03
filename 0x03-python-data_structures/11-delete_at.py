#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    b4 = list(my_list[0 : idx])
    aftr = list(my_list[idx + 1:])
    new = b4 + aftr
    for idx in range(len(new)):
        my_list[idx] = new[idx]
    del my_list[-1]
    return my_list
