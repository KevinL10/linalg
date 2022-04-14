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

	def test_multiply_scalar(self):
		expected = Matrix([[-4, 4], [-2, -10], [0, -8], [-2, -6]])
		self.assertEqual(expected, self.m2 * -2)

		expected = Matrix([[4, 0, 0], [-4, 4, 0], [0, -4, 4]])
		self.assertEqual(expected, self.m1 * 4)

	def test_multiply_vector(self):
		self.assertEqual(Vector([1, 3, 5]), self.m1 * Vector([1, 4, 9]))
		self.assertEqual(Vector([4, 8, 4, 6]), self.m2 * Vector([3, 1]))

	def test_multiply_matrix_square(self):
		m1 = Matrix([[1, 1], [2, -1]])
		m2 = Matrix([[2, 2], [3, 4]])
		expected = Matrix([[5, 6], [1, 0]])
		self.assertEqual(expected, m1 * m2)

	def test_multiply_matrix_nonsquare(self):
		A = Matrix([[5, -1, -4], [3, 0, 1]])
		expected = Matrix([[4, -2, -10], [20, -1, 1], [12, 0, 4], [14, -1, -1]])
		self.assertEqual(expected, self.m2 * A)

	def test_get_column(self):
		self.assertEqual([1, -1, 0], self.m1.column(0))
		self.assertEqual([-2, 5, 4, 3], self.m2.column(1))

	def test_get_column_unchanged(self):
		col = self.m1.column(1)
		col.append(-1)
		self.assertEqual(self.m1, Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]]))

	def test_get_row_unchanged(self):
		row = self.m1[0]
		row.append(-1)
		self.assertEqual(self.m1, Matrix([[1, 0, 0], [-1, 1, 0], [0, -1, 1]]))

	def test_identity(self):
		sz = 5
		identity = Matrix.identity(sz)
		for i in range(sz):
			for a in range(sz):
				self.assertEqual(i == a, identity[i][a])

	def test_augment(self):
		expected = Matrix([[2, -2, 2], [1, 5, 3], [0, 4, 4], [1, 3, 5]])
		self.assertEqual(self.m2.augment(Vector([2, 3, 4, 5])), expected)

		expected = Matrix([[1, 0, 0, 5], [-1, 1, 0, -2], [0, -1, 1, -9]])
		self.assertEqual(self.m1.augment(Vector([5, -2, -9])), expected)

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
 
	# test for infinite solutions
	def test_solve_singular_infinite(self):
		pass

	# test for no solutions
	def test_solve_singular_none(self):
		pass


if __name__ == '__main__':
    unittest.main()