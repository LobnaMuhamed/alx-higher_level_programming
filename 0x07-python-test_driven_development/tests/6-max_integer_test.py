#!/usr/bin/python3

import unittest

"""
unittests for function def max_integer(list=[])
"""

max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):
    """
    unittests for function def max_integer(list=[])
    """
    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([34, 12, -23, 24]), 34)
        self.assertEqual(max_integer([10, 12, -53, 49]), 49)
        self.assertEqual(max_integer([-20, 12, 23, -12]), 23)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([12]), 12)
        self.assertEqual(max_integer([]), None)
if __name__ == '__main__':
    unittest.main()
