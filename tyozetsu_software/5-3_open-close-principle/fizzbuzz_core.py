import abc


class ReplaceRuleInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def match(self, carry: str, n: int) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def apply(self, carry: str, n: int) -> str:
        raise NotImplementedError()


class NumberConverter:
    def __init__(self, rules: list[ReplaceRuleInterface]):
        self.rules = rules

    def convert(self, n: int) -> str:
        carry = ""
        for rule in self.rules:
            if rule.match(carry, n):
                carry = rule.apply(carry, n)
        return carry
