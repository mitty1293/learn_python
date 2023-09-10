import unittest
from unittest.mock import MagicMock

from src.core.number_converter import NumberConverter
from src.spec.pass_through_rule import PassThroughRule
from src.spec.cyclic_number_rule import CyclicNumberRule


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        rule1 = CyclicNumberRule(3, "Fizz")
        rule2 = CyclicNumberRule(5, "Buzz")
        rule3 = PassThroughRule()
        fizzbuzz = NumberConverter([rule1, rule2, rule3])

        self.assertEqual("1", fizzbuzz.convert(1))
        self.assertEqual("2", fizzbuzz.convert(2))
        self.assertEqual("Fizz", fizzbuzz.convert(3))
