import unittest
from menu import *
from new_game import *

class TestMenu(unittest.TestCase):
    def setUp(self):
        def for_testing():
            return True
        self.func = for_testing()

    def test_instantiate_menuitem(self):
        self.assertIsInstance(MenuItem('1', 'New game', self.func), MenuItem)

    def test_menuitem(self):
        i = MenuItem('1', 'New game', self.func)
        self.assertEqual(i.text, 'New game')

    def test_instantiate_menu(self):
        self.assertIsInstance(Menu([1, 2, 3]), Menu)

    def test_menu(self):
        m = Menu([1, 2, 3])
        self.assertEqual(m.choices, [1, 2, 3])

    def test_menu_representation(self):
        i = MenuItem('1', 'New game', self.func)
        i2 = MenuItem('2', 'Save game', self.func)
        m = Menu([i, i2])
        self.assertEqual(str(m), '1 New game\n2 Save game')

    def test_invoke_choice(self):
        i = MenuItem('1', 'New game', self.func)
        i2 = MenuItem('2', 'Save game', self.func)
        m = Menu([i, i2])
        self.assertEqual(m.invoke('1'), True)


unittest.main()
