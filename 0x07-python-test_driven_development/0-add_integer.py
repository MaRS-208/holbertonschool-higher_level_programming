#!/usr/bin/python3
"""
    module
"""


def add_integer(a, b=98):
    """ adds integers """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be in integer")
    a = int(a)
    b = int(b)
    return a + b 
