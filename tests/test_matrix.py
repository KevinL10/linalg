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

if __name__ == '__main__':
    unittest.main()