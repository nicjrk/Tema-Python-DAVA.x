import sqlite3
from datetime import datetime
import os


# Creeaza calea catre fisierul .db
DB_NAME = os.path.join(os.path.dirname(__file__), 'operations.db')


def init_db():
    """Creeaza tabela requests daca nu exista deja"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT NOT NULL,
            parameters TEXT,
            result TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()


def log_request(operation: str, parameters: str, result: str):
    """Insereaza o operatie in tabela requests"""
    timestamp = datetime.now().isoformat()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO requests (operation, parameters, result, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (operation, parameters, result, timestamp))
    conn.commit()
    conn.close()
