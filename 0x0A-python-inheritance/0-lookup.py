#!/usr/bin/python3
"""
    module
"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object """
    if type(obj):
        return dir(obj)
