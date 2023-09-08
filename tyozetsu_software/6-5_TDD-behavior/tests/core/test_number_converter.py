import unittest

from src.core.number_converter import NumberConverter

class TestNumberConverter(unittest.TestCase):
    def test_convert(self):
        fizzbuzz = NumberConverter()
        self.assertEqual("1", fizzbuzz.convert(1))
        self.assertEqual("2", fizzbuzz.convert(2))
        self.assertEqual("Fizz", fizzbuzz.convert(3))
        self.assertEqual("4", fizzbuzz.convert(4))
        self.assertEqual("Buzz", fizzbuzz.convert(5))
        self.assertEqual("Fizz", fizzbuzz.convert(6))
        self.assertEqual("Buzz", fizzbuzz.convert(10))
        self.assertEqual("FizzBuzz", fizzbuzz.convert(15))
        self.assertEqual("FizzBuzz", fizzbuzz.convert(30))
