#!/usr/bin/env python
import unittest

from code import calculate


class CalculateTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calculate(1), 0.127)

    def test_5(self):
        self.assertEqual(calculate(5), 0.619)
        
    def test_10(self):
        self.assertEqual(calculate(10), 1.234)


if __name__ == '__main__':
    unittest.main()
