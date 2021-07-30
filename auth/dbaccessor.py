#!/usr/bin/env python3
import sqlite3

class DbAccessor:
    def __init__(self, db_file: str) -> None:
        """Constructor

        Args:
            db_file (str): SQLite database file path
        """
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, user_id, user_pass, salt)")
        self.conn.commit()

    def fetch_from_db(self, user_id: str) -> sqlite3.Row:
        """Select a row of data from 'user' table

        Args:
            user_id (str): The user_id of the record to be fetched

        Returns:
            sqlite3.Row: fetchone()は
                         * user_idが存在する場合は紐づくレコードをsqlite3.Rowオブジェクト（like 辞書）で返す。
                           sqlite3.Row[column_name] で要素にアクセス可能
                         * 存在しない場合はNoneを返す。
        
        Note:
            本メソッドはレコード取得までが範囲であるため、呼び出し元で存在判定することが望ましい。

            user_idが存在する場合、返り値であるRowオブジェクトは空ではないのでTrue判定される。
            user_idが存在しない場合、返り値であるNoneはpythonではFalse判定される。
        """
        self.cur.execute('SELECT * FROM user WHERE user_id = ?', (user_id,))
        return self.cur.fetchone()

    def store_to_db(self, user_id: str, user_pass: str, salt: str) -> None:
        """Insert a row of data to 'user' table

        Args:
            user_id (str): To be inserted in column 'user_id'
            user_pass (str): To be inserted in column 'user_pass'
            salt (str): To be inserted in column 'salt'
        """
        self.cur.execute('INSERT INTO user (user_id, user_pass, salt) VALUES (?, ?, ?)', (user_id, user_pass, salt))
        self.conn.commit()

    def delete_from_db(self, user_id: str) -> None:
        """Delete a row from 'user' table

        Args:
            user_id (str): The user_id of the record to be deleted
        """
        self.cur.execute('DELETE FROM user WHERE user_id = ?', (user_id,))
        self.conn.commit()