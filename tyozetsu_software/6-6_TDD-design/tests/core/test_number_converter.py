import unittest
from unittest.mock import MagicMock

from src.core.number_converter import NumberConverter

class TestNumberConverter(unittest.TestCase):
    def test_convert_with_empty_rules(self):
        fizzbuzz = NumberConverter([])
        self.assertEqual("", fizzbuzz.convert(1))
    
    def test_convert_with_single_rule(self):
        rule = MagicMock()
        rule.replace.return_value = "Replaced"

        fizzbuzz = NumberConverter([rule])
        self.assertEqual("Replaced", fizzbuzz.convert(1))
