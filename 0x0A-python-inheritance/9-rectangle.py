#!/usr/bin/python3
"""Full rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle """
    
    def __init__(self, width, height):
        """ init """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """ area """
        return (self.height * self.width)

    def __str__(self):
        """str"""
        return (f"[Rectangle] {self.width}/{self.height}")
