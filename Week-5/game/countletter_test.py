import unittest
from countletter import letter_counter

class LetterCounterTest(unittest.TestCase):
    def test_if_exist(self):
        self.assertEqual(letter_counter(''), {})

    def test_same_letters(self):
        self.assertEqual(letter_counter('a'), {'a': 1})
        self.assertEqual(letter_counter('aa'), {'a': 2})

    def test_different_letters(self):
        self.assertEqual(letter_counter('b'), {'b': 1})

    def test_distinct_letters(self):
        self.assertEqual(letter_counter('ab'), {'a': 1, 'b': 1})
        self.assertEqual(letter_counter('abab'), {'a': 2, 'b': 2})
        self.assertEqual(letter_counter('aaacbbb'), {'a': 3, 'b': 3, 'c': 1})
        self.assertEqual(letter_counter('hablaaahami'), {'a': 5, 'b': 1, 'h': 2, 'm': 1, 'l': 1, 'i': 1})
        self.assertEqual(letter_counter('kacsa'), {'a': 2, 'k': 1, 'c': 1, 's': 1 })

unittest.main()
