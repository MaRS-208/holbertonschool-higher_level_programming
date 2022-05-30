#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle """

    def __init__(self, width, height):
        """ init """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
