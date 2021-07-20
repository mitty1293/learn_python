#!/usr/bin/env python3
import secrets, string
import dbaccessor, user

class AccountManager:
    def __init__(self, db_file: str) -> None:
        self.chars: str = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters + string.digits + '_' + '-' + '!'
        self.cur = dbaccessor.DbAccessor(db_file)

    def signup(self, user_id: str, user_pass: str) -> bool:
        new_user = user.User()
        new_user.user_id = user_id
        new_user.user_pass = user_pass

        salt: str = "".join(secrets.choice(self.chars) for i in range(32))
        new_user.create_hash(new_user.user_pass, salt)

        is_succeeded: bool
        if self.cur.store_to_db(new_user.user_id, new_user.hashed_pass, salt):
            return(is_succeeded := True)
        return (is_succeeded := False)

    def signin(self, user_id: str, user_pass: str) -> bool:
        existing_user = user.User()
        existing_user.user_id = user_id
        existing_user.user_pass = user_pass

        is_succeeded: bool
        if (db_data := self.cur.fetch_from_db(existing_user.user_id)):
            existing_user.create_hash(existing_user.user_pass, db_data["salt"])
            if db_data["user_pass"] == existing_user.hashed_pass:
                return (is_succeeded := True)
        return (is_succeeded := False)
