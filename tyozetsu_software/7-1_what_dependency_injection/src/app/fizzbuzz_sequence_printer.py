from abc import ABC, abstractmethod

from src.core.number_converter import NumberConverter
from src.spec.pass_through_rule import PassThroughRule
from src.spec.cyclic_number_rule import CyclicNumberRule


class OutputInterface(ABC):
    @abstractmethod
    def write(self, data: str) -> None:
        raise NotImplementedError


class FizzBuzzSequencePrinter:
    def __init__(self, fizzbuzz: NumberConverter, output: OutputInterface) -> None:
        self.fizzbuzz = fizzbuzz
        self.output = output

    def print_range(self, begin: int, end: int) -> None:
        for i in range(begin, end + 1):
            text = self.fizzbuzz.convert(i)
            formatted_text = f"{i:d} {text}"
            self.output.write(formatted_text)
