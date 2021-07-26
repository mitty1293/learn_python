#!/usr/bin/env python3
import hashlib

class InputValue():
    def __init__(self, user_id, user_pass) -> None:
        self._user_id = String(user_id)
        self._user_pass = String(user_pass)

    def user_id(self):
        return self._user_id.return_value()

    def hashing_pass(self, salt):
        return self._user_pass.hashing_str(salt)

class String():
    def __init__(self, value) -> None:
        self.value: str = value

    def return_value(self):
        return self.value

    def hashing_str(self, salt):
        return hashlib.sha256((self.value + salt).encode()).hexdigest()