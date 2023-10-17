#!/usr/bin/python3
"""
    unit test for class square
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Instantiation of test cases for the Square class."""

    def test_is_base(self):
        """testing base"""
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        """testing rectangle"""
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        """test no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """test one argument"""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """test two arguments"""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """test three arguments"""
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """test four arguments"""
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        """test more than four arguments"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


if __name__ == "__main__":
    unittest.main()
