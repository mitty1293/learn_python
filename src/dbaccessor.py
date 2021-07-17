#!/usr/bin/env python3
import sqlite3

class DbAccessor:
    def __init__(self, db_file) -> None:
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def aaa():
        pass