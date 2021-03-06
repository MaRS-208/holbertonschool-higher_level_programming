#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x getter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y getter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area"""
        return self.width * self.height

    def display(self):
        """displays rectangle"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """str representation"""
        s1 = f"[Rectangle] ({self.id}) "
        s2 = f"{self.x}/{self.y} - {self.width}/{self.height}"
        return s1 + s2

    def update(self, *args, **kwargs):
        """updates instance"""
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        """dictionary representation"""
        r = {'x': self.x,
             'y': self.y,
             'id': self.id,
             'height': self.height,
             'width': self.width}
        return r
