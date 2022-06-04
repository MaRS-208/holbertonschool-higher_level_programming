#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)
