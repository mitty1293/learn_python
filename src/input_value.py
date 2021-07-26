#!/usr/bin/env python3
import hashlib

class InputValue():
    def __init__(self, user_id, user_pass) -> None:
        self._user_id = String(user_id)
        self._user_pass = String(user_pass)

    def user_id(self):
        return self._user_id.return_value()

    def hashed_pass(self, salt):
        return self._user_pass.hashing_str(salt)

class String():
    def __init__(self, value) -> None:
        self.value: str = value

    def return_value(self):
        return self.value

    def hashing_str(self, salt):
        """[summary]
        Args:
            salt (str): [description]
        Note:
            str.encode(): strをutf-8でエンコードしたbytesオブジェクトを返す
            hashlib.sha256(bytes): sha256で暗号化されたhashオブジェクトを返す
            hash.hexdigest: hashオブジェクトの16進形式文字列を返す
        """
        return hashlib.sha256((self.value + salt).encode()).hexdigest()