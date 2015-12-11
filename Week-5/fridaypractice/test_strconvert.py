import unittest
from strconverter import *

class TestConvertes(unittest.TestCase):
    def test_isempty(self):
        stri = Mystring('')
        self.assertEqual(stri.str_converter(), '')

    def test_ones(self):
        stri = Mystring('din')
        stri2 = Mystring('eeffgg')
        self.assertEqual(stri.str_converter(), '(((')
        self.assertEqual(stri2.str_converter(), '))))))')

    def test_composit(self):
        stri = Mystring("recede")
        stri2 = Mystring('Success')
        stri3 = Mystring('(( @')
        self.assertEqual(stri.str_converter(), '()()()')
        self.assertEqual(stri2.str_converter(), ')())())')
        self.assertEqual(stri3.str_converter(), '))((')


unittest.main()
