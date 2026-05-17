import os
import sqlite3

os.makedirs("database", exist_ok=True)

DATABASE = "database/system.db"


def connect():
    return sqlite3.connect(DATABASE)


def create_tables():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        health_plan TEXT,
        city TEXT,
        phone TEXT,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()