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
