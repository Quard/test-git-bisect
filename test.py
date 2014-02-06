#!/usr/bin/env python
import unittest

from code import calculate


class CalculateTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calculate(1), 0.123)

    def test_5(self):
        self.assertEqual(calculate(5), 0.615)
        
    def test_10(self):
        self.assertEqual(calculate(10), 1.23)


if __name__ == '__main__':
    unittest.main()
