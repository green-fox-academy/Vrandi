import unittest
import func

class TestFunc(unittest.TestCase):
    def test_apply_func(self):
        array= [1,2,3]
        self.assertEqual(func.adder(array), [2, 3, 4])
    def test_generators(self):
       def _adder(n):
           for i in range(n):
               yield i
       g =_adder(5)
       print(g.__next__())
       print(g.__next__())

unittest.main()
