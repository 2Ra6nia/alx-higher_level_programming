#!/usr/bin/python3
""" module for square class """
from models.rectangle import Rectangle


class square(Rectangle):
    """ square class"""


    def __init__(self, size, x=0, y=0, id=None):
        """constrctor """
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """sring info about square"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)



    @property
    def size(self):
        """size of the square"""
        return self.width


    @size.setter
    def size(self, value):
        self.width = value
        self.height = value



    def __update(self, id=None, size=None, x=None, y=None):
        """update instance attrbutes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y


    def update(self, *args, **kwargs):
        """update instance attrbutes via args, kwargs"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)



    def to_dictionary(self):
        """ return dicitionary for square class"""
        return ("id": self.id, "size": self.size,
                "x": self.x, "y": self.y)
