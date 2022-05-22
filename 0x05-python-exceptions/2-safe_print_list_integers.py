#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    s = 0
    while c < x:
        try:
            print("{:d}".format(my_list[c]), end="")
            s += 1
            c += 1
        except (TypeError, ValueError):
            c += 1
    print("")
    return (nprint)
