import math
from vector import *


# angle between v and w (in radians)
def angle_between(v, w):
	return math.acos(v.dot(w) / (v.length() * w.length()))


# cauchy schwarz inequality (v dot w <= ||v|| * ||w||)
def cauchy_schwarz(v, w):
	return v.dot(w) <= v.length() * w.length()


# triangle inequality (||v + w|| <= ||v|| + ||w||)
def triangle_inequality(v, w):
	return (v + w).length() <= v.length() + w.length()