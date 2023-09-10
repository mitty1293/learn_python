from src.app.fizzbuzz_sequence_printer import FizzBuzzSequencePrinter
from src.app.fizzbuzz_sequence_printer import OutputInterface
from src.core.replace_rule_interface import ReplaceRuleInterface
from src.core.number_converter import NumberConverter
from src.spec.cyclic_number_rule import CyclicNumberRule
from src.spec.pass_through_rule import PassThroughRule


class FizzBuzzAppFactory:
    def create_fizz_rule(self) -> ReplaceRuleInterface:
        return CyclicNumberRule(3, "Fizz")

    def create_buzz_rule(self) -> ReplaceRuleInterface:
        return CyclicNumberRule(5, "Buzz")

    def create_pass_through_rule(self) -> ReplaceRuleInterface:
        return PassThroughRule()

    def create_fizzbuzz(self) -> NumberConverter:
        return NumberConverter([
            self.create_fizz_rule(),
            self.create_buzz_rule(),
            self.create_pass_through_rule(),
        ])

    def create_output(self) -> OutputInterface:
        return ConsoleOutput()

    def create(self) -> FizzBuzzSequencePrinter:
        return FizzBuzzSequencePrinter(self.create_fizzbuzz(), self.create_output())


class ConsoleOutput(OutputInterface):
    def write(self, data: str) -> None:
        print(data)
