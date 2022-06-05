#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def __str__(self):
        """str representation"""
        s1 = f"[Square] ({self.id}) "
        s2 = f"{self.x}/{self.y} - {self.size}"
        return s1 + s2


