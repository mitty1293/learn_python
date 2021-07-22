#!/usr/bin/env python3
import hashlib

class UserInfo():
    def __init__(self) -> None:
        self.user_id: str = "user_id"
        self.user_pass: str = "user_pass"

class HashedInfo():
    def __init__(self) -> None:
        self.hashed_pass: str = "hashed_pass"

class InputValue():
    def __init__(self) -> None:
        self.user_info = UserInfo()
        self.hashed_info = HashedInfo()
        # self.user_id:str = ""
        # self.user_pass:str = ""
        # self.hashed_pass:str = ""


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