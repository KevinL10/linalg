from vector import *

class Matrix:
	# initialize with 2d list of values
	def __init__(self, data):
		self.__data = data


	# note: override equality check for matrices/vectors with floats
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__data == other.__data
		return False


	# data is safe to change
	def __getitem__(self, idx):
		return self.__data[idx][:]


	# multiply by a vector (A * x)
	def __mul__(self, v):
		assert len(self.__data[0]) == len(v)
		return Vector([Vector(self.__data[i]).dot(v) for i in range(len(self.__data))])


	# returns the column at idx
	def column(self, idx):
		return [self.__data[i][idx] for i in range(len(self.__data))]


	# returns (rows, columns)
	def size(self):
		return len(self.__data), len(self.__data[0])