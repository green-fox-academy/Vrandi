import unittest
from sudoku import *

class TestValidateNumbers(unittest.TestCase):
	def test_empty(self):
		self.assertEqual(validate_numbers([]), False)

	def test_nine(self):
		self.assertEqual(validate_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), True)
		self.assertEqual(validate_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1]), True)
		self.assertEqual(validate_numbers([9, 9, 9, 9, 5, 4, 3, 2, 1]), False)

	def test_if_not_number(self):
		self.assertEqual(validate_numbers(['a', 'b', 'c', 3, 4, 5, 7]), False)

	def test_seven(self):
		self.assertEqual(validate_numbers([1, 2, 3, 4, 5, 6, 7]), False)

unittest.main()