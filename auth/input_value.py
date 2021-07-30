#!/usr/bin/env python3
import hashlib

class InputValue():
    def __init__(self, user_id: str, user_pass: str) -> None:
        """Constructor

        Args:
            user_id (str): User ID of the account
            user_pass (str): Password of the account
        """
        self._user_id = StringValue(user_id)
        self._user_pass = StringValue(user_pass)

    def user_id(self) -> str:
        """Return a value of self._user_id

        Returns:
            str: A value of self._user_id
        """
        return self._user_id.return_value()

    def hashed_pass(self, salt: str) -> str:
        """Hashing a value of self._user_pass

        Args:
            salt (str): A string to randomizes the output of the password hash

        Returns:
            str: Hash string of self._user_pass
        """
        return self._user_pass.hashing_str(salt)

class StringValue():
    def __init__(self, value: str) -> None:
        """Constructor

        Args:
            value (str): Value
        """
        self.value: str = value

    def return_value(self) -> str:
        """Return a value of class "StringValue"

        Returns:
            str: A value of class "StringValue"
        """
        return self.value

    def hashing_str(self, salt: str) -> str:
        """Hashing a value of class "StringValue"
        Args:
            salt (str): A string to randomizes the output of the password hash

        Returns:
            str: Hash string of class "StringValue"

        Note:
            str.encode(): Return a bytes object with str encoded in utf-8
            hashlib.sha256(bytes_object): Return a SHA-256 hash object
            hash_object.hexdigest(): Return as a string object containing only hexadecimal digits
        """
        return hashlib.sha256((self.value + salt).encode()).hexdigest()