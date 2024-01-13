#!/usr/bin/python3
""" module for rectangle class"""
from models.base import Base


class Rectangle(Base):
	"""  Rectangle class"""
	
	
	def __init__(self, width, height, x=0, y=0, id=None)
		""" constructor """
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y


	@property
	def width(self):
		""" width of rectangle"""
		return self.__width
		
		
	@width.setter
	def width(self, value):
		self.__width = value


	@property
	def height(self):
		""" height of rectangle"""
		return self.__height

	@height.setter
	def height(self, value):
		self.__height = value

		
	@property
	def x(self):
		""" x of rectangle"""
		return self.__x


	@x.setter
	def x(self, value):
		self.__x = value


	@property
	def y(self):
		""" y of rectangle"""
		return self.__y


	@y.setter
	def y(self, value):
		self.__y = value



        def validate_integer(self, name, vlue, eg=True):
		""" method for validate the value """
		if type(value) != int:
			raise TypeError("{} must be integer".format(name))
		if eg and value < 0:
			raise ValueError("{} must be >= 0".format(name))
		elif not eg and value <= 0:
			raise ValueError("{} must be > 0".format(name))



        def area(self):
              """ computes the area"""
              return self.width *  self.height
