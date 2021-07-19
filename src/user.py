#!/usr/bin/env python3
import hashlib

class User():
    def __init__(self) -> None:
        self.user_id = ""
        self.user_pass = ""
        self.hashed_pass = ""

    def create_hash(self, data: str, salt: str) -> None:
        """[summary]

        Args:
            data (str): [description]
            salt (str): [description]

        Note:
            str.encode(): strをutf-8でエンコードしたbytesオブジェクトを返す
            hashlib.sha256(bytes): sha256で暗号化されたhashオブジェクトを返す
            hash.hexdigest: hashオブジェクトの16進形式文字列を返す
        """
        data = data + salt
        self.hashed_pass = hashlib.sha256(data.encode()).hexdigest()
        # hashlib.pbkdf2_hmac(hash_name, password, salt, iterations)