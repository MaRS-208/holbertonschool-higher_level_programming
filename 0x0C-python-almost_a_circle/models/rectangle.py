#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""


class Rectangle:
    """Rectangle class"""
    __width -> width
    __height -> height
    __x -> x
    __y -> y

    def __init__(self, width, height, x=0, y=0, id=None)
        """init"""
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if type(width) <= 0:
            raise ValueError("width must be > 0")
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if type(height) <= 0:
            raise ValueError("height must be > 0")
        if x <= 0:
            raise ValueError("x must be >= 0")
        if y <= 0:
            raise ValueError("y must be >= 0")

