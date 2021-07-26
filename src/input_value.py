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
        self._user_id = UserId(user_id)
        self._user_pass = UserPass(user_pass)

    def create_hash(self, salt):
        return self._user_pass.create_hash(salt)