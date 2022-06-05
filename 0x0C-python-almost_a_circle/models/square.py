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

    def update(self, *args, **kwargs):
        """updates instance"""
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """dictionary representation"""
        r = {   'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
        return r
