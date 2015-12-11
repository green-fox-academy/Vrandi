import unittest
import func

class TestFunc(unittest.TestCase):
    def test_apply_func(self):
        array= [1,2,3]
        self.assertEqual(func.adder(array), [2, 3, 4])

    def test_filter_array(self):
        array = [x for x in range(0, 10)]
        self.assertEqual(func.filterArray(array), [0,3,6,9])

unittest.main()
