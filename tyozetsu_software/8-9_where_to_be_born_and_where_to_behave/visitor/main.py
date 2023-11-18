from abc import ABC, abstractmethod


class VisitableInterface(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Node(VisitableInterface):
    def accept(self, visitor):
        visitor(self)


class Branch(Node):
    def __init__(self):
        self.children = []

    def accept(self, visitor):
        super().accept(visitor)
        for child in self.children:
            child.accept(visitor)
