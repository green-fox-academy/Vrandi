import unittest
from torpedofield import *

class TestField(unittest.TestCase):
    def setUp(self):
        self.field = [
            [1,1,0,1,0,0,1,1,1,1],
            [0,0,0,1,0,0,0,0,0,0],
            [1,0,0,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,0,0,0,1],
            [0,0,0,0,0,1,0,0,0,1],
            [1,1,0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,1,1]
        ]

    def test_Instantiate(self):
        self.assertIsInstance(Field(1, 2, 'stat'), Field)

    def test_instance(self):
        f = Field(0, 1, 'stat')
        self.assertEqual(f.xindex, 0)
        self.assertEqual(f.yindex, 1)

    def test_statuschange(self):
        f = Field(0, 1, False)
        f.statuschanger()
        self.assertEqual(f.status, True)

unittest.main()
