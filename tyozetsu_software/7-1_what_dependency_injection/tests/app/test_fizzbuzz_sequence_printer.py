import unittest
from unittest.mock import MagicMock, call

from src.app.fizzbuzz_sequence_printer import FizzBuzzSequencePrinter
from src.app.fizzbuzz_sequence_printer import OutputInterface
from src.core.number_converter import NumberConverter


class TestFizzBuzzSequencePrinter(unittest.TestCase):
    def test_print_none(self):
        converter = MagicMock(spec=NumberConverter)
        converter.convert.assert_not_called()
        output = MagicMock(spec=OutputInterface)
        output.write.assert_not_called()

        printer = FizzBuzzSequencePrinter(converter, output)
        printer.print_range(0, -1)

    def test_ptint_1to3(self):
        converter = MagicMock(spec=NumberConverter)
        converter.convert.side_effect = lambda x: {1: "1", 2: "2", 3: "Fizz"}.get(x)
        results = [converter.convert(1), converter.convert(2), converter.convert(3)]
        expected_results = ["1", "2", "Fizz"]
        for result, expected in zip(results, expected_results):
            assert result == expected

        output = MagicMock(spec=OutputInterface)
        expected_args = [
            "1 1\n",
            "2 2\n",
            "3 Fizz\n"
        ]
        for arg in expected_args:
            output.write(arg)
        output.write.assert_has_calls([call(arg) for arg in expected_args])

        printer = FizzBuzzSequencePrinter(converter, output)
        printer.print_range(1, 3)
