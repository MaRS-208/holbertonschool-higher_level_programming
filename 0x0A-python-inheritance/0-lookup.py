#!/usr/bin/python3
"""
    lookup
"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object """
    if type(obj):
        return list(dir(obj))
