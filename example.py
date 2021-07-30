#!/usr/bin/env python3
import auth

def main():
    am = auth.AccountManager("/your/sqlite/database/file/path")
    sign: int = int(input("Sign up:0, Sign in:1 -> "))
    if sign == 1:
        print("Sign in progress...")
        existing_user_id: str = input("Enter your ID ->")
        existing_user_pass: str = input("Enter your Password ->")
        if am.signin(existing_user_id, existing_user_pass):
            print("Sign in success")
            return
        print("Sign-in faii.")
    else:
        print("Sign up progress...")
        new_user_id: str = input("Enter the new ID ->")
        new_user_pass: str = input("Enter the new Password ->")
        if am.signup(new_user_id, new_user_pass):
            print("You have signed up successfully.")
            return 
        print("Sign-up fail. ID is already used by another account.")

if __name__ == '__main__':
    main()