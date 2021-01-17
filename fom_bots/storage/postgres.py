import os
from contextlib import contextmanager

import psycopg2

from config import DATABASE_URL, BASE_DIR


@contextmanager
def postgres_conn(commit: bool = False):
    conn = get_conn()
    yield conn
    if commit:
        conn.commit()
    conn.close()


@contextmanager
def postgres_cursor(commit: bool = False):
    with postgres_conn(commit) as conn:
        cursor = conn.cursor()
        yield cursor
        cursor.close()


def get_conn():
    return psycopg2.connect(DATABASE_URL)


def init_db():
    with open(os.path.join(BASE_DIR, 'storage/ddl.sql'), 'r') as f:
        ddl = f.read()
    with postgres_cursor(True) as cursor:
        cursor.execute(ddl)
