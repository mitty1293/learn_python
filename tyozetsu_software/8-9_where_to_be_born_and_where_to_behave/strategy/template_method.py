from abc import abstractmethod

from expression_interface import ExpressionInterface


class AbstractExpression(ExpressionInterface):
    def __init__(self):
        self.vars = None

    def set_variables(self, vars):
        if self.validate(vars):
            raise ValueError("Invalid variables")
        self.vars = vars

    def evaluate(self):
        if self.vars is None:
            raise ValueError("Variables not set")
        return self.calculate()

    @abstractmethod
    def validate(self, vars):
        pass

    @abstractmethod
    def calculate(self):
        pass


class PlusExpression(AbstractExpression):
    def validate(self, vars):
        return len(vars) != 2

    def calculate(self):
        return self.vars[0] + self.vars[1]

# 他にMinusExpressionなどもあると仮定


expression = PlusExpression()
expression.set_variables([1.1, 2.2])
print(expression.evaluate())  # Output: 3.3
