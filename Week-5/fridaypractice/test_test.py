import unittest
from names import *

class Testnames(unittest.TestCase):
    def setUp(self):
        self.names = [{ 'id': 1, 'name': 'John'},
                { 'id': 2, 'name': 'Molly'},
                { 'id': 3, 'name': 'Jane'}]

    def test_instantiate(self):
        self.assertIsInstance(MyMagic([]), MyMagic)

    def test_names_as_list_when_empty(self):
        subject = MyMagic([])
        self.assertEqual(subject.names_as_list(), [])

    def test_names_as_list(self):
        subject = MyMagic(names)
        self.assertEqual(subject.names_as_list(), ['John', 'Molly', 'Jane'])

    def test_j(self):
        subject = MyMagic(names)
        self.assertEqual(subject.names_with_J(), ['John', 'Jane'])


unittest.main()
