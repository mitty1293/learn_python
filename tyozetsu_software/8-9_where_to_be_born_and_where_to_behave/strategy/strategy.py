from abc import ABC, abstractmethod
from typing import List, Optional

from expression_interface import ExpressionInterface


class CalculationStrategyInterface(ABC):
    @abstractmethod
    def validate(self, vars: List[float]) -> bool:
        pass

    @abstractmethod
    def calculate(self, vars: List[float]) -> float:
        pass


class Expression(ExpressionInterface):
    def __init__(self):
        self.vars: Optional[List[float]] = None
        self.calculation_strategy: Optional[CalculationStrategyInterface] = None

    def set_calculation_strategy(self, strategy: CalculationStrategyInterface) -> None:
        self.calculation_strategy = strategy

    def set_variables(self, vars: List[float]) -> None:
        if self.calculation_strategy.validate(vars):
            raise ValueError("Invalid variables")
        self.vars = vars

    def evaluate(self) -> float:
        if self.vars is None or self.calculation_strategy is None:
            raise ValueError("Variables or calculation strategy not set")
        return self.calculation_strategy.calculate(self.vars)


class PlusCalculationStrategy(CalculationStrategyInterface):
    def validate(self, vars: List[float]) -> bool:
        return len(vars) == 2

    def calculate(self, vars: List[float]) -> float:
        return vars[0] + vars[1]

# 他にMinusCalculationStrategyなどもあると仮定


# 使用例
expression = Expression()
expression.set_calculation_strategy(PlusCalculationStrategy())
expression.set_variables([1.1, 2.2])
print(expression.evaluate())  # Output: 3.3
