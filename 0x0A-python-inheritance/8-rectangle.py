#!/usr/bin/python3
"""Rectangle"""


class Rectangle():
    """ rectangle """

    def __init__(self, width, height):
        """ init """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
