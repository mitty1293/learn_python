from src.core.replace_rule_interface import ReplaceRuleInterface


class CyclicNumberRule(ReplaceRuleInterface):
    def __init__(self, base: int, replacement: str) -> None:
        self.base = base
        self.replacement = replacement

    def apply(self, carry: str, n: int) -> str:
        return f"{carry}{self.replacement}"

    def match(self, carry: str, n: int) -> bool:
        return n % self.base == 0
