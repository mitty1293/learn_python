import unittest
from unittest.mock import MagicMock

from src.core.number_converter import NumberConverter


class TestNumberConverter(unittest.TestCase):
    def create_mock_rule(self, expected_number: int, expected_carry: str, match_result: bool, replacement: str):
        moke_rule = MagicMock()

        def return_apply(arg1, arg2):
            return replacement

        def return_match(arg1, arg2):
            return match_result

        moke_rule.apply.side_effect = return_apply
        moke_rule.match.side_effect = return_match
        return moke_rule

    def test_convert_with_empty_rules(self):
        fizzbuzz = NumberConverter([])
        self.assertEqual("", fizzbuzz.convert(1))

    def test_convert_with_single_rule(self):
        mock_rule = self.create_mock_rule(
            expected_number=1,
            expected_carry="",
            match_result=True,
            replacement="Replaced",
        )
        fizzbuzz = NumberConverter([mock_rule])
        self.assertEqual("Replaced", fizzbuzz.convert(1))

    def test_convert_composisting_rule_results(self):
        mock_rule1 = self.create_mock_rule(
            expected_number=1,
            expected_carry="",
            match_result=True,
            replacement="Fizz",
        )
        mock_rule2 = self.create_mock_rule(
            expected_number=1,
            expected_carry="Fizz",
            match_result=True,
            replacement="FizzBuzz",
        )
        fizzbuzz = NumberConverter([mock_rule1, mock_rule2])
        self.assertEqual("FizzBuzz", fizzbuzz.convert(1))

    def test_convert_skipping_unmatched_rules(self):
        mock_rule1 = self.create_mock_rule(
            expected_number=1,
            expected_carry="",
            match_result=False,
            replacement="Fizz",
        )
        mock_rule2 = self.create_mock_rule(
            expected_number=1,
            expected_carry="",
            match_result=False,
            replacement="Buzz",
        )
        mock_rule3 = self.create_mock_rule(
            expected_number=1,
            expected_carry="",
            match_result=True,
            replacement="1",
        )
        fizzbuzz = NumberConverter([mock_rule1, mock_rule2, mock_rule3])
        self.assertEqual("1", fizzbuzz.convert(1))
