#!/usr/bin/env python3
import secrets, string
from auth.dbaccessor import DbAccessor
from auth.input_value import InputValue

class AccountManager:
    def __init__(self, db_file: str) -> None:
        """Constractor

        Args:
            db_file (str): SQLite database file path
        """
        self.chars: str = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters + string.digits + '_' + '-' + '!'
        self.dbaccessor = DbAccessor(db_file)

    def signup(self, user_id: str, user_pass: str) -> bool:
        """[summary]

        Args:
            user_id (str): [description]
            user_pass (str): [description]

        Returns:
            bool: True if the data is stored, False otherwise
        """
        new_user = InputValue(user_id, user_pass)
        salt: str = "".join(secrets.choice(self.chars) for i in range(32))

        is_succeeded: bool
        if self.dbaccessor.fetch_from_db(new_user.user_id()):
            return (is_succeeded := False)
        self.dbaccessor.store_to_db(new_user.user_id(), new_user.hashed_pass(salt), salt)
        return(is_succeeded := True)

    def signin(self, user_id: str, user_pass: str) -> bool:
        existing_user = InputValue(user_id, user_pass)

        is_succeeded: bool
        if (db_data := self.dbaccessor.fetch_from_db(existing_user.user_id())):
            return (is_succeeded := (True if db_data["user_pass"] == existing_user.hashed_pass(db_data["salt"]) else False))
        return (is_succeeded := False)

    def delete_user(self, user_id: str, user_pass: str) -> bool:
        """[summary]

        Args:
            user_id (str): [description]
            user_pass (str): [description]

        Returns:
            bool: True if the data is deleted, False otherwise
        """
        is_deleted: bool
        if self.signin(user_id, user_pass):
            self.dbaccessor.delete_from_db(user_id)
            return (is_deleted := True)
        return (is_deleted := False)
