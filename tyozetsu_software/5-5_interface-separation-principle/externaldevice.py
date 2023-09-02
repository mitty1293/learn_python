from connection import InternalBus, USBDeviceInterface
from operation import KeyboardInterface, PointerDeviceInterface


# クラスを定義
class USBKeyboard(KeyboardInterface, USBDeviceInterface):
    def connect(self, bus):
        pass

    def type_key(self, code):
        print(f"You type '{code}' using a USB keyboard")


class USBMouse(PointerDeviceInterface, USBDeviceInterface):
    def connect(self, bus):
        pass

    def move_cursor(self, direction, distance):
        print(f"direction={direction}, distance={distance}")
