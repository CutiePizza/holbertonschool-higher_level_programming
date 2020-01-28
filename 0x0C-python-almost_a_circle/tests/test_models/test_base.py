#!/usr/bin/python3
import unittest
from models.base import Base
"""
Test Module for Base class
"""

class TestBase(unittest.TestCase):
    """
    TestBase for Base
    """
    def test(self):
        """
        Tests when d is given or not
        """
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base(15)
        self.assertEqual(b.id, 15)
        b = Base()
        self.assertEqual(b.id, 4)
        b = Base(2)
        self.assertEqual(b.id, 2)
        b = Base(-3)
        self.assertEqual(b.id, -3)
