#!/usr/bin/env python3
import secrets, string
from dbaccessor import DbAccessor
from input_value import InputValue

class AccountManager:
    def __init__(self, db_file: str) -> None:
        """Constractor

        Args:
            db_file (str): SQLite database file path
        """
        self.db_file = db_file
        self.chars: str = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters + string.digits + '_' + '-' + '!'
        self.cur = DbAccessor(self.db_file)

    def signup(self, user_id: str, user_pass: str) -> bool:
        new_user = InputValue(user_id, user_pass)

        salt: str = "".join(secrets.choice(self.chars) for i in range(32))
        hashed_pass = new_user.hashing_pass(salt)

        is_succeeded: bool
        if self.cur.store_to_db(new_user.user_id(), hashed_pass, salt):
            return(is_succeeded := True)
        return (is_succeeded := False)

    def signin(self, user_id: str, user_pass: str) -> bool:
        existing_user = InputValue(user_id, user_pass)

        is_succeeded: bool
        if (db_data := self.cur.fetch_from_db(existing_user.user_id())):
            hashed_pass = existing_user.hashing_pass(db_data["salt"])
            return (is_succeeded := (True if db_data["user_pass"] == hashed_pass else False))
        return (is_succeeded := False)  
