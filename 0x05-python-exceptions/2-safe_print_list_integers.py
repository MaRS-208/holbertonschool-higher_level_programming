#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    large = 0
    nprint = 0
    while large < x:
        try:
            print("{:d}".format(my_list[large]), end="")
            nprint += 1
            large += 1
        except (TypeError, ValueError):
            large += 1
    print("")
    return (nprint)
