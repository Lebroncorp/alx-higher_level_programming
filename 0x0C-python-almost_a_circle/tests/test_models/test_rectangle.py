#!/usr/bin/python3
"""
    unit tests for class Rectangle
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases ofor class rectangle"""
    def test_init_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_init_neg_values(self):
        with self.assertRaises(ValueError):
            Rectangle(-7, -3)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)


if __name__ == "__main__":
    unittest.main()
