import unittest
from anagramm import is_anagramm

class Test_is_anagramm(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(is_anagramm('', ''), True)
        
    def test_difference(self):
        self.assertEqual(is_anagramm('a', ''), False)

    def test_anagramm(self):
        self.assertEqual(is_anagramm('ab', 'ba'), True)
        self.assertEqual(is_anagramm('abc', 'bac'), True)

unittest.main()
