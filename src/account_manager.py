#!/usr/bin/env python3
import secrets, string
import dbaccessor, user

class AccountManager:
    chars: str = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters + string.digits + '_' + '-' + '!'
    cur = dbaccessor.DbAccessor("/auth/data/user.db")

    def signup(self, user_id: str, user_pass: str):
        new_user = user.User()
        new_user.user_id = user_id
        new_user.user_pass = user_pass

        salt: str = "".join(secrets.choice(self.chars) for i in range(32))
        new_user.create_hash(new_user.user_pass, salt)

        is_succeeded: bool
        if self.cur.store_to_db(new_user.user_id, new_user.hashed_pass, salt):
            return(is_succeeded := True)
        return (is_succeeded := False)
