#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """my int"""
    def __eq__(self, other):
        """eq"""
        return self.real != other.real
    def __ne__(self, other):
        """ne"""
        return not self.__eq__(other)
