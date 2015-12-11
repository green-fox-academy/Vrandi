import unittest
from monster import Monster

class TestMonster(unittest.TestCase):
    def test_existance(self):
        monster = Monster('Mike Wasowski', 20, 1)

    def test_inheritance(self):
        monster = Monster('Mike Wasowski', 20, 1)
        self.assertEqual(monster.hp, 20)

    def test_strike(self):
        monster = Monster('Mike Wasowski', 20, 1)
        other = Monster('Randall', 10, 2)
        monster.strike(other)
        self.assertEqual(monster.hp, 22)
        self.assertEqual(other.hp, 9)

unittest.main()
