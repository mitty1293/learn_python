from abc import ABC, abstractmethod


# インターフェースを定義
class USBDeviceInterface(ABC):
    @abstractmethod
    def connect(self, bus):
        pass


# クラスを定義
class USBPort:
    def __init__(self):
        self.internal_bus = InternalBus()  # 内部バスを初期化する必要があります

    def plug(self, device):
        device.connect(self.internal_bus)


class InternalBus:
    pass
