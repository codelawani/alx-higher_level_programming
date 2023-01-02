#!/usr/bin/python3
class Rectangle:
	def __init__(self, width=0, height=0) -> None:
		self.width = width
		self.height = height
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		if not isinstance(width, int):
			raise TypeError('width must be an integer')
		elif width < 0:
			raise ValueError('width must be >= 0')
		self._width = width
	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		if not isinstance(height, int):
			raise TypeError('height must be an integer')
		elif height < 0:
			raise ValueError('height must be >= 0')
		self._height = height