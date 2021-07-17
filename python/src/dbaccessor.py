#!/usr/bin/env python3
import sqlite3

class DbAccessor():
    def __init__(self) -> None:
        self.conn = sqlite3.connect("/data/user.db")
        self.cur = self.conn.cursor()

    def aaa():
        pass