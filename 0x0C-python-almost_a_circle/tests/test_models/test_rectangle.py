#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""
Test Module for Rectangle class
"""


class TestBase(unittest.TestCase):
    """
    TestBase for Base
    """
    def test_zero(self):
        """
        Tests for rectangle
        """
        if __name__ == "main":
            R = Rectangle(10, 2)
            self.assertEqual(R.id, 1)
            R = Rectangle(2, 10)
            self.assertEqual(R.id, 2)
            R = Rectangle(10, 2, 0, 0, 12)
            self.assertEqual(R.id, 12)
            R = Rectangle(-2, 1)
            self.assertEqual(R.id, 3)
        with self.assertRaises(TypeError):
            R = Rectangle()

    def test_two(self):
        """
        Second round of tests
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(10, "2")

        with self.assertRaises(ValueError):
            R1 = Rectangle(0, 3)

        with self.assertRaises(ValueError):
            R1 = Rectangle(-5, 6)

        with self.assertRaises(ValueError):
            R1 = Rectangle(2, -5)

        with self.assertRaises(TypeError):
            R1 = Rectangle("2", 3)

        with self.assertRaises(ValueError):
            R1 = Rectangle(5, 10, 0, -9)

        with self.assertRaises(ValueError):
            R1 = Rectangle(5, 10, -3, 5)

        with self.assertRaises(TypeError):
            R1 = Rectangle(5, 10, "hello", 2)

        with self.assertRaises(TypeError):
            R2 = Rectangle(5, 10, 2, "helloe")

        R1 = Rectangle(5, 10, 0, 2, 3)
        self.assertEqual(R1.id, 3)

        with self.assertRaises(TypeError):
            R1 = Rectangle()

    def test_three_area(self):
        """
        third set of tests
        """
        r1 = Rectangle(3, 2)
        n = r1.area()
        self.assertEqual(n, 6)

        r2 = Rectangle(2, 10)
        n = r2.area()
        self.assertEqual(n, 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        n = r3.area()
        self.assertEqual(n, 56)

    def test_four_display(self):
        """
        four set of tests
        """
        r1 = Rectangle(4, 6)
        r1.display()

    def test_five_str(self):
        """
        fivth set of tests
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        f = print(r1)

    def test_seven_update(self):
        """
        seven's set of sets
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        with self.assertRaises(ValueError):
            r1.update(6, 2, 3, -4, 5)

        with self.assertRaises(TypeError):
            r1.update(1, "hello", 3, 4, 5)

        with self.assertRaises(TypeError):
            r1.update(1, 2, 3, 5, "7")
