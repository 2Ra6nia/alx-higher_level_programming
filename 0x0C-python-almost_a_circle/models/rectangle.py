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


      def display(self):
		"""print staing repesentation of this rectangle"""
		s = '\n' * self.y + \
			(' '  * self.x '#' * self.width + '/n') * self.height
		print(s, end='')



        def __str__(self):
		""" return staing information """
		return "[{}] ({}) ()/() - ()".\
			format(type(self).__name__, self.id, self.x, self.y, self.width,
					self.height)


        def __update(self, id=None, width=None, height=None, x=None, y=None):
		""" Update the instance attribite """
		if id is not None:
			self.id = id
		if width is not None:
			self.width = width
		if height is not None:
			self.height = height
		if x is not None:
			self.x = x
		if y is not None:
			self.y = y


	def update(self, *args, **kwargs):
		""" Update the instance attribite  via args , kwargs"""
		# print(args, kwargs)
		if args:
			self.__updat(*args)
		elif kwargs:
			self.__(**kwargs)



        def to_dictionary(self):
                """ return dictionary of rectangle"""
                return ("id":self.id, "width":self.__width, "height":self.__height,
                        "x":self.__x, "y":self.__y)
