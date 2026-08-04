import sqlite3

DATABASE_PATH = 'contacts.db'

CREATE_CONTACTS_TABLE = '''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    created_date TEXT NOT NULL
);
'''


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as conn:
        conn.execute(CREATE_CONTACTS_TABLE)
        conn.commit()


def save_contact(name, email, subject, message, created_date):
    with get_connection() as conn:
        conn.execute(
            'INSERT INTO contacts (name, email, subject, message, created_date) VALUES (?, ?, ?, ?, ?)',
            (name, email, subject, message, created_date)
        )
        conn.commit()
