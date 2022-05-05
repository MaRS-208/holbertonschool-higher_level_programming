#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_new_dictionary = {}
    for key, value in a_dictionary.items():
        a_new_dictionary[key] = value * 2
    return a_new_dictionary
