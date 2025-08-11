import sqlite3
import os


DB_NAME = os.path.join(
    os.path.dirname(__file__), '..', 'storage', 'operations.db'
)


def show_all():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM requests")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


if __name__ == '__main__':
    show_all()
