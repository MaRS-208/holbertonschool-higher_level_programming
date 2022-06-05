#!/usr/bin/python3
"""Write the first class Base"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """JSON string representation"""
        if list_dictionaries == None:
            return "[]"
        return list_dictionaries
