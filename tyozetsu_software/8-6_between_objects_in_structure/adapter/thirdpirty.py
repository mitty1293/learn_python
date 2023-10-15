from abc import ABC, abstractmethod


class VendorGraphicsInterface(ABC):
    @abstractmethod
    def line(self, x0: int, y0: int, x1: int, y1: int):
        pass
