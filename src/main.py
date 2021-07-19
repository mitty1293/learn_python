#!/usr/bin/env python3
import user

def main():
    print("Sign up:0, Sign in:1 -> ")
    sign: int = input()
    if sign:
        print("Sign in progress...")
        sign_in()
    else:
        print("Sign up progress...")
        sign_up()

def sign_in():
    pass

def sign_up():
    print("Enter the new ID ->")
    new_user_id: str = input()
    print("Enter the new Password ->")
    new_user_pass: str = input()

    new_user = user.User(new_user_id, new_user_pass)
    new_user.encrypt()

if __name__ == '__main__':
    main()