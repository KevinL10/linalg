import math

class Vector:
	def __init__(self, data):
		self.__data = data


	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__data == other.__data
		return False


	def __str__(self):
		return str(self.__data)


	def __len__(self):
		return len(self.__data)


	def __setitem__(self, key, value):
		self.__data[key] = value

	def __getitem__(self, key):
		return self.__data[key]

	# vector addition (u + v)
	def __add__(self, v):
		assert len(self) == len(v)
		return Vector([self[i] + v[i] for i in range(len(v))])


	# vector subtraction (u - v)
	def __sub__(self, v):
		assert len(self) == len(v)
		return Vector([self[i] - v[i] for i in range(len(v))])


	# scalar multiplication (v * 5)
	def __mul__(self, c):
		return Vector([self[i] * c for i in range(len(self))])


	# scalar multiplication (5 * v)
	def __rmul__(self, c):
		return self * c

	# returns vector as a list copy
	def list(self):
		return [i for i in self.__data]

	# dot product (u dot v)
	def dot(self, v):
		return sum([self[i] * v[i] for i in range(len(v))])


	# length (||v||)
	def length(self):
		return self.dot(self) ** 0.5