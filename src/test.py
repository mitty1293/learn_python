#!/usr/bin/env python3
import hashlib

class UserInfo:
    def __init__(self) -> None:
        self._user_info = {}

    def refer_to(self, value):
        return self._user_info[value]

    def add(self, user_id, user_pass):
        self._user_info["id"] = user_id
        self._user_info["pass"] = user_pass

    def create_hash(self, salt):
        return hashlib.sha256((self._user_info["pass"] + salt).encode()).hexdigest()