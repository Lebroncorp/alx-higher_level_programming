#!/usr/bin/python3
"""
    unit test for the class Base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Instantiation of all test cases of Base class"""

    def test_init(self):
        """test cases for attributes
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)

        b3 = Base()
        self.assertEqual(b3.id, 2)
    """

    def test_None_id(self):
        """test for none id"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """test for unique id"""
        self.assertEqual(13, Base(13).id)


if __name__ == "__main__":
    unittest.main()
