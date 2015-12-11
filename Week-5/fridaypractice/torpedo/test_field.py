import unittest
from torpedofield import *

class TestField(unittest.TestCase):
    def test_instantiate_field(self):
        self.assertIsInstance(Field(1, 2, 'stat'), Field)

    def test_instance(self):
        f = Field(0, 1, 'stat')
        self.assertEqual(f.xindex, 0)
        self.assertEqual(f.yindex, 1)

    def test_statuschange(self):
        f = Field(0, 1, False)
        f.statuschanger()
        self.assertEqual(f.status, True)

    def test_instantiate_shipfield(self):
        self.assertIsInstance(Shipfield(1, 2, 'stat'), ShipField)


unittest.main()
