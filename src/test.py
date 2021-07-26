#!/usr/bin/env python3
import hashlib

class StringValue:
    def __init__(self) -> None:
        self._str = ""

    def assign(self, string_):
        self._str = string_

    def create_hash(self, salt):
        return hashlib.sha256((self._str + salt).encode()).hexdigest()