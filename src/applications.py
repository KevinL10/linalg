import math
from vector import *
from matrix import *

# angle between v and w (in radians)
def angle_between(v, w):
	return math.acos(v.dot(w) / (v.length() * w.length()))


# cauchy schwarz inequality (v dot w <= ||v|| * ||w||)
def cauchy_schwarz(v, w):
	return v.dot(w) <= v.length() * w.length()


# triangle inequality (||v + w|| <= ||v|| + ||w||)
def triangle_inequality(v, w):
	return (v + w).length() <= v.length() + w.length()


# matrices for sum and difference of 3 numbers
def difference_sum_matrices():
	v = Vector([1, 4, 9])
	sumMatrix = Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
	diffMatrix = Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])
	
	assert diffMatrix * (sumMatrix * v) == v