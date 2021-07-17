#!/usr/bin/env python3
import sqlite3
from typing import List

class DbAccessor:
    def __init__(self, db_file) -> None:
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def fetch_from_db(self, tbl_name, target_column, key) -> List:
        self.cur.execute("SELECT * FROM %s WHERE %s = %s;", (tbl_name, target_column, key))
        results = self.cur.fetchall()
        return results

    def store_to_db(self, tbl_name, stored_id, stored_pass, stored_salt):
        self.cur.execute("INSERT INTO user (id, pass, salt) VALUES (%s, %s, %s);", (stored_id, stored_pass, stored_salt))
        self.cur.commit()
        return 0