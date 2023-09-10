from src.core.replace_rule_interface import ReplaceRuleInterface


class PassThroughRule(ReplaceRuleInterface):
    def apply(self, carry: str, n: int) -> str:
        return str(n)

    def match(self, carry: str, n: int) -> bool:
        return carry == ""
