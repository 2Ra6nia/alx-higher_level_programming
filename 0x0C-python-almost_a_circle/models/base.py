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
            __nb_objects += 1
            self.id = Base.__nb_objects
            
