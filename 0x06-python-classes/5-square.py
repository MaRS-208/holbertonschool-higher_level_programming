#!/usr/bin/python3
""" class """


class Square:
    """Creating/defining Square class"""
    def __init__(self, size=0):
        """Initializes the class with the proper characteristics"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for j in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")
