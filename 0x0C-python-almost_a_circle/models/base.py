#!/usr/bin/python3
"""Write the first class Base"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs"""
        list_ne = []
        if list_objs is not None:
            for i in list_objs:
                list_ne.append(i.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(cls.to_json_string(list_ne))

    @staticmethod
    def from_json_string(json_string):
        """JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a dictionary"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                list_dic = cls.from_json_string(f.read())
                list_o = []
                for j in list_dic:
                    list_o.append(cls.create(**j))
                return list_o
        except FileNotFoundError:
            return []
