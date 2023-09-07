import unittest
import sys

from src.math import Math

class TestMath(unittest.TestCase):
    def test_min(self):
        math = Math()
        self.assertEqual(0, math.min(0, 1))
        self.assertEqual(0, math.min(1, 0))
        self.assertEqual(-1, math.min(0, -1))
        self.assertEqual(-1, math.min(-1, 0))
        self.assertEqual(0, math.min(0, 0))
        self.assertEqual(0, math.min(0, sys.maxsize))
        self.assertEqual(-sys.maxsize, math.min(0, -sys.maxsize))
    
    def test_max(self):
        math = Math()
        self.assertEqual(1, math.max(0, 1))
        self.assertEqual(1, math.max(1, 0))
        self.assertEqual(0, math.max(0, -1))
        self.assertEqual(0, math.max(-1, 0))
        self.assertEqual(0, math.max(0, 0))
        self.assertEqual(sys.maxsize, math.max(0, sys.maxsize))
        self.assertEqual(0, math.max(0, -sys.maxsize))
