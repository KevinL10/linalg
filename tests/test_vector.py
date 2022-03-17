# import src modules...
import sys
sys.path.append('../src/')

import unittest
from vector import *



class TestVector(unittest.TestCase):
	def setUp(self):
		self.v1 = Vector([5, -2, 17, 4])
		self.v2 = Vector([6, -12, 3, -4])

	def test_str(self):
		self.assertEqual("[5, -2, 17, 4]", str(self.v1))

	def test_len(self):
		self.assertEqual(4, len(self.v1))

	def test_get_item(self):
		self.assertEqual(17, self.v1[2])
		self.assertEqual(6, self.v2[0])

	def test_add(self):
		self.assertEqual(Vector([11, -14, 20, 0]), self.v1 + self.v2)
		self.assertEqual(Vector([11, -14, 20, 0]), self.v2 + self.v1)

	def test_sub(self):
		self.assertEqual(Vector([-1, 10, 14, 8]), self.v1 - self.v2)
		self.assertEqual(Vector([1, -10, -14, -8]), self.v2 - self.v1)

	def test_mul(self):
		self.assertEqual(Vector([15, -6, 51, 12]), self.v1 * 3)
		self.assertEqual(Vector([-12, 24, -6, 8]), -2 * self.v2)


if __name__ == '__main__':
    unittest.main()