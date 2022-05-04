#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = []
    for x in my_list:
        if x != search:
            my_new_list.append(x)
        else:
            my_new_list.append(replace)
    return my_new_list
