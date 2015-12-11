import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard('Merlin', 40, 10, 20)

    def test_inheritance(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.manna, 20)

    def test_strike_have_manna(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        other = Wizard('Ursula', 40, 10, 20)
        wizard.strike(other)
        self.assertEqual(wizard.manna, 15)
        self.assertEqual(other.hp, 10)

    def test_strike_no_manna(self):
        wizard = Wizard('Merlin', 40, 10, 4)
        other = Wizard('Ursula', 40, 10, 20)
        wizard.strike(other)
        self.assertEqual(wizard.manna, 4)
        self.assertEqual(other.hp, 37)


unittest.main()
