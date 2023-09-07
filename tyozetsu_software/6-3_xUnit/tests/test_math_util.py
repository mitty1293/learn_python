import unittest
import sys

from src.math_util import MathUtil

class Test_athUtil(unittest.TestCase):
    def test_saturate(self):
        math_util = MathUtil()
        self.assertEqual(2, math_util.saturate(2, 1, 3))
        self.assertEqual(1, math_util.saturate(0, 1, 3))
        self.assertEqual(3, math_util.saturate(4, 1, 3))
        self.assertEqual(1, math_util.saturate(1, 1, 3))
        self.assertEqual(3, math_util.saturate(3, 1, 3))
