from abc import ABC, abstractmethod


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class DrawingInterface(ABC):
    @abstractmethod
    def start_at(self, p: Point):
        pass

    @abstractmethod
    def line_to(self, p: Point):
        pass
