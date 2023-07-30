from fizzbuzz_core import ReplaceRuleInterface


class CyclicNumberRule(ReplaceRuleInterface):
    """倍数に関するルール

    Args:
        ReplaceRuleInterface (_type_): インターフェース
    """
    def __init__(self, base: int, replacement: str):
        self.base = base
        self.replacement = replacement

    def match(self, carry: str, n: int) -> bool:
        return n % self.base == 0

    def apply(self, carry: str, n: int) -> str:
        return f"{carry}{self.replacement}"


class PassThroughRule(ReplaceRuleInterface):
    """条件に該当しない場合のルール

    Args:
        ReplaceRuleInterface (_type_): インターフェース
    """
    def match(self, carry: str, n: int) -> bool:
        return carry == ""

    def apply(self, carry: str, n: int) -> str:
        return str(n)
