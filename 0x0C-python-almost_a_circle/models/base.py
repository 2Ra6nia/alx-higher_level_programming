#!/usr/bin/python3
""" module for base class"""


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
