#!/usr/bin/python3
"""
    module
"""

def add_attribute(a_class, a_name, a_value):
    """ adds attributes """
    if not hasattr(a_class, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(a_class, a_name, a_value)
