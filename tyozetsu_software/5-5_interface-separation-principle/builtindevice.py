from operation import KeyboardInterface, PointerDeviceInterface


# クラスを定義
class BuiltinKeyboard(KeyboardInterface):
    def type_key(self, code):
        print(f"You type '{code}' using a Built-in keyboard")


class BuiltinTrackpad(PointerDeviceInterface):
    def move_cursor(self, direction, distance):
        print(f"direction={direction}, distance={distance}")
