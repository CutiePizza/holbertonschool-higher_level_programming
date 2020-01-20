import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 0, 5, 4]), 5)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(["a", "aa", "aaa", "aaaa"]), "aaaa")
        self.assertAlmostEqual(max_integer([-1, -2, -3, 0]), 0)
