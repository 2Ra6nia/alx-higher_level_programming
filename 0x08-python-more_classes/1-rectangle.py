#!/usr/bin/python3
""""
Defining  a Class Rectangle
"""

class Rectangle:
    """Initialization of rectangle"""
    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height


    @property
    def width(self):
        """getter for private instance width"""
        return self.__width


    @width.setter
    def width(self, value):
        """setter for private instance width"""
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """getter for the private instance height"""
        return self.___height


    @height.setter
    def height(self, value):
        """setter for private instance height"""
        if type(value) is not int:
            raise typeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
