from abc import ABC, abstractmethod


class ReplaceRuleInterface(ABC):
    @abstractmethod
    def apply(self, carry: str, n: int) -> str:
        raise NotImplementedError

    @abstractmethod
    def match(self, carry: str, n: int) -> bool:
        raise NotImplementedError
