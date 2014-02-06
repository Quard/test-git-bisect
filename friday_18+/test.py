#!/usr/bin/python
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from code import findboobs

IMAGE = os.path.join(os.path.dirname(__file__), 'res/image.jpg')

class FounderTestCase(unittest.TestCase):

    def test_founder(self):
        self.assertEqual(len(findboobs(IMAGE)), 2)


if __name__ == '__main__':
    unittest.main()
