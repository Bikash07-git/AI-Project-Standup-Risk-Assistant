import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / 'project_assistant.db'


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            team TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            owner TEXT NOT NULL,
            team TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS updates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            project_id INTEGER,
            update_date TEXT NOT NULL,
            completed TEXT,
            today TEXT,
            blocker TEXT,
            dependency TEXT,
            additional_context TEXT,
            ai_analysis TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            update_id INTEGER,
            status TEXT,
            edited_value TEXT,
            reviewed_by TEXT,
            reviewed_at TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_review(update_id, status, reviewed_by='manager', edited_value=None):
    conn = get_connection()
    now = datetime.utcnow().isoformat() + 'Z'
    conn.execute(
        '''
        INSERT INTO reviews (update_id, status, edited_value, reviewed_by, reviewed_at)
        VALUES (?, ?, ?, ?, ?)
        ''',
        (update_id, status, edited_value, reviewed_by, now),
    )
    conn.commit()
    review_id = conn.execute('SELECT last_insert_rowid() AS id').fetchone()['id']
    conn.close()
    return {'id': review_id, 'status': status, 'reviewed_by': reviewed_by, 'reviewed_at': now}


def list_reviews():
    conn = get_connection()
    rows = conn.execute(
        '''
        SELECT id, update_id, status, edited_value, reviewed_by, reviewed_at
        FROM reviews
        ORDER BY reviewed_at DESC
        '''
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
