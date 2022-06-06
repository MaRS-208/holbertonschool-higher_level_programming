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
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs"""
        if list_objs is None or len(list_objs) == 0:
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(None))
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary()
                for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """creates a dictionary"""
        
        return cls(**dictionary)

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        pass
