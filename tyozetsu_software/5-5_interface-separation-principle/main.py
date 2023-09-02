from builtindevice import BuiltinKeyboard, BuiltinTrackpad
from connection import USBPort
from externaldevice import USBKeyboard, USBMouse
from operation import PCOperator

builtin_keyboard = BuiltinKeyboard()
usb_mouse = USBMouse()
operator = PCOperator(builtin_keyboard, usb_mouse)
operator.input_text("abcde")
operator.point_at(1, 2)
