import unittest
from menu_class import *
from character import *

class TestMenu(unittest.TestCase):
    def setUp(self):
        def for_testing():
            return True

        self.func = for_testing

    def test_instantiate_menuitem(self):
        self.assertIsInstance(MenuItem('1', 'New game', self.func), MenuItem)

    def test_menuitem(self):
        i = MenuItem('1', 'New game', self.func)
        self.assertEqual(i.name, 'New game')

    def test_instantiate_menu(self):
        self.assertIsInstance(Menu([1, 2, 3]), Menu)

    def test_menu(self):
        m = Menu([1, 2, 3])
        self.assertEqual(m.items, [1, 2, 3])

    def test_menu_representation(self):
        i = MenuItem('1', 'New game', self.func)
        i2 = MenuItem('2', 'Save game', self.func)
        m = Menu([i, i2])
        self.assertEqual(str(m), '\n1 New game\n2 Save game\n')

    def test_invoke_choice(self):
        i = MenuItem('1', 'New game', self.func)
        i2 = MenuItem('2', 'Save game', self.func)
        m = Menu([i, i2])
        result = m.invoke()
        self.assertEqual(result, True)

    def test_instantiate_user(self):
        self.assertIsInstance(Character(), Character)

unittest.main()
