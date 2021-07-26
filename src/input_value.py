#!/usr/bin/env python3
import hashlib

class UserId():
    def __init__(self, user_id) -> None:
        self.user_id: str = user_id

class UserPass():
    def __init__(self, user_pass) -> None:
        self.user_pass: str = user_pass

    def create_hash(self, salt):
        return hashlib.sha256((self.user_pass + salt).encode()).hexdigest()

class InputValue():
    def __init__(self, user_id, user_pass) -> None:
        self.user_id = UserId(user_id)
        self.user_pass = UserPass(user_pass)

    def create_hash(self, salt: str) -> None:
        """[summary]

        Args:
            salt (str): [description]

        Note:
            str.encode(): strをutf-8でエンコードしたbytesオブジェクトを返す
            hashlib.sha256(bytes): sha256で暗号化されたhashオブジェクトを返す
            hash.hexdigest: hashオブジェクトの16進形式文字列を返す
        """
        self.hashed_pass = hashlib.sha256((self.user_pass + salt).encode()).hexdigest()
        # hashlib.pbkdf2_hmac(hash_name, password, salt, iterations)