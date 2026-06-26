import sqlite3

DB_NAME = "students.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll_number TEXT,
            marks_math INTEGER,
            marks_science INTEGER,
            marks_english INTEGER
        )
    """)
    conn.commit()
    conn.close()