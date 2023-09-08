from abc import ABC, abstractmethod


class ReplaceRuleInterface(ABC):
    @abstractmethod
    def replace(self, n: int) -> str:
        pass
