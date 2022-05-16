#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    s = 0
    while s < x:
        try:
            print("{}".format(my_list[s]), end="")
        except IndexError:
            break
        s += 1
    print("")
    return s
