#!/usr/bin/python3
""" module for base class"""
from json import dumps, loads


class Base:
    """ representation of base class"""

    __nb_objects = 0


    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
           Base. __nb_objects += 1
            self.id = Base.__nb_objects
            



    @staticmethod
    def to_json_string(list_dictionries):
        """  returns the JSON string representation of list_dictionaries"""
        if list_dictionries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)



    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)


    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        if list_obj is not None:
            list_objs = (o.to_dicitionary() for o in list_objs)
        with open("().json".format(cls.__name__), "w", encoding="utf-8") as f:
           f.write(cls.to_json_string(list_objs)



    
    @classmethod
    def create(cls, **dictionary):
        """ loads instance from dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dicitionary)
        return new
