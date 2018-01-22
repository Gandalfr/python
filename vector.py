#import math
from math import sqrt,acos,pi
from decimal import Decimal,getcontext

getcontext().prec = 30

class Vector(object):
	def __init__(self,coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple([Decimal(x) for x in coordinates])
			self.dimension = len(coordinates)

		except ValueError:
			raise ValueError('The coordinates must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def __str__(self):
		return 'Vector:{}'.format(self.coordinates)

	def __eq__(self,v):
		return self.coordinates == v.coordinates

	def plus(self,v):
		#new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
		new_coordinates = []
		n = len(self.coordinates)
		for i in range(n):
			new_coordinates.append(self.coordinates[i]+v.coordinates[i])

		return Vector(new_coordinates)

	def minus(self,v):
		new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
		return Vector(new_coordinates)

	def times_scalar(self,c):
		new_coordinates = [Decimal(c)*x for x in self.coordinates]
		return Vector(new_coordinates)

	def magnitude(self):
		#magnitude = 0
		#for x in self.coordinates:
		#	magnitude += x*x
		#return math.sqrt(magnitude)

		coordinates_squared = [x**2 for x in self.coordinates]
		return sqrt(sum(coordinates_squared))

	# calculate unit
	def direction(self):
		u = self
		magnitude = self.magnitude()
		new_coordinates = [x*(1/magnitude) for x in self.coordinates]
		
		return Vector(new_coordinates)

	def normalized(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(Decimal('1.0')/magnitude)
		except ZeroDivisionError:
			raise Exception('Cannot normalize the zero vector')

	def dotProduct(self,v):
		new_coordinates = [x*y for x,y in zip(self.coordinates,v.coordinates)]

		sum = 0
		for i in new_coordinates:
			sum +=i
		return sum
	
	def angle(self,v):
		m1 = self.magnitude()
		m2 = v.magnitude()
		dotP = self.dotProduct(v)
		print m1,m2,dotP
		try:
			result = acos(dotP/(m1*m2))
			return result
		except ZeroDivisionError:
			raise Exception('Cannot caculate angle with the zero vector')






