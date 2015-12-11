import unittest
from decorator import *

class TestKnife(unittest.TestCase):
    def test_exist(self):
        knife = Knife()
    def test_rusty_effect(self):
        weapon = Rusty(TestWeapon())
        self.assertEqual(weapon.demage(), 5)


class TestWeapon:
    def demage(self):
        return 10

if __name__ == '__main__':
    unittest.main()
