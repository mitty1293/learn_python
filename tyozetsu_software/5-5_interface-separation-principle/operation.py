from abc import ABC, abstractmethod


# インターフェースを定義
class KeyboardInterface(ABC):
    @abstractmethod
    def type_key(self, code):
        raise NotImplementedError


class PointerDeviceInterface(ABC):
    @abstractmethod
    def move_cursor(self, x, y):
        raise NotImplementedError


# クラスを定義
class PCOperator:
    def __init__(self, keyboard, pointer_device):
        self.keyboard = keyboard
        self.pointer_device = pointer_device

    def input_text(self, codes):
        for code in codes:
            self.keyboard.type_key(code)

    def point_at(self, x, y):
        # direction と distance を x, y から考えて…
        # direction = 0.0  # 仮の値
        # distance = 0.0   # 仮の値
        direction = f"direction from {x} and {y}"
        distance = f"distance from {x} and {y}"
        self.pointer_device.move_cursor(direction, distance)
