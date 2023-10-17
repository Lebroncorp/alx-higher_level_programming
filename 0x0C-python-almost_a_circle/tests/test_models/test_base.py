#!/usr/bin/python3
"""
    unit test for the class Base
"""

import unittest
from models.base import Base

class TestBase(unittest.Testcase):
    """Instantiation of all test cases of Base class"""
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(13, Base(13).id)

if __name__ == "__main__":
    unittest.main()
