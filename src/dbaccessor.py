#!/usr/bin/env python3
import sqlite3
from typing import List, Tuple

class DbAccessor:
    def __init__(self, db_file: str) -> None:
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def fetch_from_db(self, key: str) -> List[Tuple[str, str, str]]:
        self.cur.execute('SELECT * FROM user WHERE user_id = ?', (key,))
        results = self.cur.fetchall()
        return results

    def store_to_db(self, stored_id: str, stored_pass: str, stored_salt: str) -> int:
        self.cur.execute('INSERT INTO user (user_id, user_pass, salt) VALUES (?, ?, ?)', (stored_id, stored_pass, stored_salt))
        self.conn.commit()
        return 0