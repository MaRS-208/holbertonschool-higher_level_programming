#!/usr/bin/python3
"""
    module
"""


class BaseGeometry():
    """class"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ int val """
        if not type(value) in int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
