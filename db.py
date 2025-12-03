# db.py
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def get_connection():
    return psycopg2.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        cursor_factory=RealDictCursor
    )

if __name__ == "__main__":
    conn = get_connection()
    cur = conn.cursor()
    # Create a test table
    cur.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO test_table (name) VALUES ('Austin');")
    cur.execute("SELECT * FROM test_table;")
    print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()
