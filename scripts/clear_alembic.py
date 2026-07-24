import sqlite3
import sys
p='instance/site.db'
try:
    conn=sqlite3.connect(p)
    cur=conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='alembic_version'")
    r=cur.fetchone()
    if r:
        cur.execute('DELETE FROM alembic_version')
        conn.commit()
        print('alembic_version cleared')
    else:
        print('no alembic_version table')
    conn.close()
except Exception as e:
    print('error:', e)
    sys.exit(1)
