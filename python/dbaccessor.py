#!/usr/bin/env python3
import sqlite3

class DbAccessor():
    def __init__(self) -> None:
        conn = sqlite3.connect()