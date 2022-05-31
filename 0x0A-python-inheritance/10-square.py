#!/usr/bin/python3
"""Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """init"""
    def __init__(self, size):
        """initializing"""
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
