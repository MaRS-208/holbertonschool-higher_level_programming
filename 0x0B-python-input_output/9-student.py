#!/usr/bin/python3
"""class Student that defines a student by"""


class Student(first_name, last_name, age)
    """class student"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of a Student instance"""
        return self.__dict__
