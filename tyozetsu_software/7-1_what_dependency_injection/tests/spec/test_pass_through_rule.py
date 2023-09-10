import unittest
from unittest.mock import MagicMock

from src.spec.pass_through_rule import PassThroughRule


class TestPassThroughRule(unittest.TestCase):
    def test_apply(self):
        rule = PassThroughRule()
        self.assertEqual("1", rule.apply("", 1))
        self.assertEqual("2", rule.apply("", 2))
        self.assertEqual("3", rule.apply("Fizz", 3))

    def test_match(self):
        rule = PassThroughRule()
        self.assertTrue(rule.match("", 0))
        self.assertFalse(rule.match("Fizz", 0))
