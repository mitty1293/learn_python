#!/usr/bin/env python3
import user, secrets, string
import dbaccessor, user

chars: str = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters + string.digits + '_' + '-' + '!'
cur = dbaccessor.DbAccessor("/auth/data/user.db")

def main():
    sign: int = int(input("Sign up:0, Sign in:1 -> "))
    if sign == 1:
        print("Sign in progress...")
        if sign_in():
            print("Sign in success")
            return
        print("Sign-in faii.")
    else:
        print("Sign up progress...")
        if sign_up():
            print("You have signed up successfully.")
            return 
        print("Sign-up fail. ID is already used by another account.")

def sign_in():
    existing_user = user.User()
    existing_user.user_id: str = input("Enter your ID ->")
    existing_user.user_pass: str = input("Enter your Password ->")

    is_succeeded: bool
    if (db_data := cur.fetch_from_db(existing_user.user_id)):
        existing_user.create_hash(existing_user.user_pass, db_data["salt"])
        if db_data["user_pass"] == existing_user.hashed_pass:
            return (is_succeeded := True)
    return (is_succeeded := False)

def sign_up():
    new_user = user.User()
    new_user.user_id: str = input("Enter the new ID ->")
    new_user.user_pass: str = input("Enter the new Password ->")

    salt: str = "".join(secrets.choice(chars) for i in range(32))
    new_user.create_hash(new_user.user_pass, salt)

    is_succeeded: bool
    if cur.store_to_db(new_user.user_id, new_user.hashed_pass, salt):
        return(is_succeeded := True)
    return (is_succeeded := False)

if __name__ == '__main__':
    main()