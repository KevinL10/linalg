# import src modules...
import sys
sys.path.append('../src/')

import unittest
from vector import *
from matrix import *
from applications import *


class TestMatrix(unittest.TestCase):
	def setUp(self):
		self.m1 = Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])
		self.m2 = Matrix([[2, -2], [1, 5], [0, 4], [1, 3]])

	def test_constructor(self):
		self.assertEqual([1, 0, 0], self.m1[0])
		self.assertEqual([0, -1, 1], self.m1[2])
		self.assertEqual(1, self.m1[1][1])
		self.assertEqual(3, self.m2[3][1])
		self.assertEqual((3, 3), self.m1.size())
		self.assertEqual((4, 2), self.m2.size())

	def test_multiply(self):
		self.assertEqual(Vector([1, 3, 5]), self.m1 * Vector([1, 4, 9]))
		self.assertEqual(Vector([4, 8, 4, 6]), self.m2 * Vector([3, 1]))

	def test_get_column(self):
		self.assertEqual([1, -1, 0], self.m1.column(0))
		self.assertEqual([-2, 5, 4, 3], self.m2.column(1))

	def test_identity(self):
		identity = Matrix.identity(5)
		for i in range(5):
			for a in range(5):
				self.assertEqual(i == a, identity[i][a])

	def test_augment(self):
		expected = Matrix([[2, -2, 2], [1, 5, 3], [0, 4, 4], [1, 3, 5]])
		self.assertEqual(self.m2.augment(Vector([2, 3, 4, 5])), expected)


	def test_solve_vector(self):
		A = Matrix([[2, 4, -2], [4, 9, -3], [-2, -3, 7]])
		b = Vector([2, 8, 10])
		expected = Vector([-1, 2, 2])
		self.assertEqual(A.solve_vector(b), expected)

	def test_solve_vector2(self):
		A = Matrix([[1, 1, 1], [1, 2, 2], [1, 2, 3]])
		b = Vector([6, 9, 10])
		expected = Vector([3, 2, 1])
		self.assertEqual(A.solve_vector(b), expected)

	# requires rearranging rows to avoid 0 pivot
	def test_solve_vector3(self):
		A = Matrix([[1, 2, 3], [2, 4, 7], [3, 5, 2]])
		b = Vector([25, 57, 23])
		expected = Vector([-2, 3, 7])
		self.assertEqual(A.solve_vector(b), expected)

if __name__ == '__main__':
    unittest.main()