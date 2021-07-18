#!/usr/bin/env python3
import sqlite3
from typing import List, Tuple

class DbAccessor:
    def __init__(self, db_file: str) -> None:
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def fetch_from_db(self, user_id: str) -> List[Tuple[str, str, str]]:
        """DBから指定したレコードを取得するメソッド

        Args:
            user_id (str): 取得したいレコードのuser_id

        Returns:
            List[Tuple[str, str, str]]: user_idが存在する場合は紐づくレコード。存在しない場合は空リスト。
        
        Note:
            本メソッドはレコード取得までが範囲であるため、呼び出し元で存在判定することが望ましい。
            
            pythonにおいて空リスト [] は False と判定される。
            その他のリストは全て True 判定となる。

            呼び出し元では以下のように判定すれば良い。
            if results:
                return results
            else:
                return "list is empty"
        """
        self.cur.execute('SELECT * FROM user WHERE user_id = ?', (user_id,))
        return self.cur.fetchall()

    def store_to_db(self, user_id: str, user_pass: str, salt: str) -> int:
        self.cur.execute('INSERT INTO user (user_id, user_pass, salt) VALUES (?, ?, ?)', (user_id, user_pass, salt))
        self.conn.commit()
        return 0