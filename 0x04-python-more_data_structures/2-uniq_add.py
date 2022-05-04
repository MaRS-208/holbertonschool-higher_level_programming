#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_new_list = []
    for x in my_list:
        if x not in my_new_list:
            my_new_list.append(x)
    return sum(my_new_list)
