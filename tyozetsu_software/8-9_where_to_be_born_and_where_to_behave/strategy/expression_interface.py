from abc import ABC, abstractmethod


class ExpressionInterface(ABC):
    @abstractmethod
    def set_variables(self, vars: list):
        pass

    @abstractmethod
    def evaluate(self):
        pass
