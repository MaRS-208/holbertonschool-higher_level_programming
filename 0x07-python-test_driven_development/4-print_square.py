#!/usr/bin/python3
"""
    module
"""


def print_square(size):
    """ prints a square """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end='')
        print()
