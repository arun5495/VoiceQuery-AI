import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('sample.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER
    )
    ''')
    conn.commit()
    cursor.execute('SELECT COUNT(*) FROM employees')
    if cursor.fetchone()[0] == 0:
        cursor.executemany('INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)', [
            ('Alice', 'HR', 70000),
            ('Bob', 'Engineering', 90000),
            ('Charlie', 'Sales', 60000)
        ])
        conn.commit()
    return conn

def execute_query(conn, query):
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return str(e)
